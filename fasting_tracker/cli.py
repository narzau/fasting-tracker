import argparse
from datetime import datetime, timedelta
import json
import os
import logging

# Set up logging
logging.basicConfig(filename=os.path.expanduser('~/.fasting_tracker_log.txt'), level=logging.DEBUG)

class FastingTracker:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.total_pause_duration = timedelta()
        self.data_dir = os.path.expanduser('~/.fasting_tracker')
        self.data_file = os.path.join(self.data_dir, 'fasting_tracker_data.json')
        self.completed_fasts_file = os.path.join(self.data_dir, 'completed_fasts.json')
        os.makedirs(self.data_dir, exist_ok=True)
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.start_time = datetime.fromisoformat(data['start_time']) if data['start_time'] else None
                self.pause_time = datetime.fromisoformat(data['pause_time']) if data['pause_time'] else None
                self.total_pause_duration = timedelta(seconds=data['total_pause_duration'])

    def save_data(self):
        data = {
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'pause_time': self.pause_time.isoformat() if self.pause_time else None,
            'total_pause_duration': self.total_pause_duration.total_seconds()
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def start(self, duration=None):
        if not self.start_time:
            now = datetime.now()
            if duration:
                self.start_time = now - duration
            else:
                self.start_time = now
            self.save_data()
            return f"🚀 Fasting timer started. Current duration: {self.get_duration()}"
        else:
            return "⚠️  Timer is already running. Use 'status' to check current time."

    def stop(self, store=True):
        if self.start_time:
            duration = self.get_duration()
            if store:
                self.save_completed_fast(duration)
                message = f"🛑 Fasting timer stopped and stored. Total duration: {duration}"
            else:
                message = f"🛑 Fasting timer stopped and discarded. Total duration: {duration}"
            
            self.start_time = None
            self.pause_time = None
            self.total_pause_duration = timedelta()
            self.save_data()
            return message
        else:
            return "⚠️  No timer is running."

    def save_completed_fast(self, duration):
        completed_fasts = []
        if os.path.exists(self.completed_fasts_file):
            with open(self.completed_fasts_file, 'r') as f:
                completed_fasts = json.load(f)
        
        completed_fasts.append({
            'end_time': datetime.now().isoformat(),
            'duration': str(duration)
        })
        
        with open(self.completed_fasts_file, 'w') as f:
            json.dump(completed_fasts, f)
        
        logging.debug(f"Saved completed fast: {duration}")

    def pause(self):
        if self.start_time and not self.pause_time:
            self.pause_time = datetime.now()
            self.save_data()
            return "⏸️  Fasting timer paused."
        else:
            return "⚠️  Timer is not running or already paused."

    def resume(self):
        if self.pause_time:
            pause_duration = datetime.now() - self.pause_time
            self.total_pause_duration += pause_duration
            self.pause_time = None
            self.save_data()
            return "▶️  Fasting timer resumed."
        else:
            return "⚠️  Timer is not paused."

    def status(self):
        if self.start_time:
            duration = self.get_duration()
            status = "paused ⏸️" if self.pause_time else "running ⏱️"
            return f"""
📊 Fasting Status:
   State: {status}
   Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}
   Current Duration: {duration}
            """
        else:
            return "ℹ️  No timer is running."

    def get_duration(self):
        if self.start_time:
            end_time = self.pause_time if self.pause_time else datetime.now()
            total_duration = end_time - self.start_time - self.total_pause_duration
            return str(total_duration).split('.')[0]  # Remove microseconds
        return "00:00:00"

    def get_history(self, limit=None):
        if os.path.exists(self.completed_fasts_file):
            with open(self.completed_fasts_file, 'r') as f:
                completed_fasts = json.load(f)
            
            # Sort fasts by end time, most recent first
            completed_fasts.sort(key=lambda x: x['end_time'], reverse=True)
            
            # Limit the number of fasts if specified
            if limit:
                completed_fasts = completed_fasts[:limit]
            
            history = "📜 Fasting History:\n"
            for i, fast in enumerate(completed_fasts, 1):
                end_time = datetime.fromisoformat(fast['end_time'])
                history += f"{i}. Ended: {end_time.strftime('%Y-%m-%d %H:%M:%S')}, Duration: {fast['duration']}\n"
            
            return history
        else:
            return "No fasting history available."

def parse_duration(duration_str):
    try:
        hours, minutes = map(int, duration_str.split(':'))
        return timedelta(hours=hours, minutes=minutes)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid duration format. Use 'HH:MM'")

def main():
    parser = argparse.ArgumentParser(description="Fasting Tracker CLI")
    parser.add_argument('action', choices=['start', 'stop', 'pause', 'resume', 'status', 'history'], help="Action to perform")
    parser.add_argument('--duration', type=parse_duration, help="Initial duration for the timer (format: 'HH:MM')")
    parser.add_argument('--discard', action='store_true', help="Discard the current fast when stopping")
    parser.add_argument('--limit', type=int, help="Limit the number of history entries to display")
    args = parser.parse_args()

    tracker = FastingTracker()
    
    if args.action == 'start':
        print(tracker.start(args.duration))
    elif args.action == 'stop':
        print(tracker.stop(not args.discard))
    elif args.action == 'pause':
        print(tracker.pause())
    elif args.action == 'resume':
        print(tracker.resume())
    elif args.action == 'status':
        print(tracker.status())
    elif args.action == 'history':
        print(tracker.get_history(args.limit))

if __name__ == "__main__":
    main()