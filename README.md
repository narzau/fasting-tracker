# Fast CLI

Fast CLI is a simple command-line interface tool to help you track your fasting schedules. It allows you to start, stop, pause, and resume fasting timers, as well as check your current fasting status and view your fasting history.

## Features

- Start a fasting timer
- Stop a fasting timer (with option to store or discard the fast)
- Pause and resume fasting timers
- Check current fasting status
- Store completed fasts for later review
- Start a timer with a specific initial duration
- View history of completed fasts

## Installation

1. Ensure you have Python 3.7 or later installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/fast-cli.git
   cd fast-cli
   ```

3. Install the package:
   ```
   pip install -e .
   ```

## Usage

After installation, you can use the `fast` command from anywhere in your terminal.

Basic commands:

- Start a fast: `fast start`
- Stop a fast: `fast stop`
- Pause a fast: `fast pause`
- Resume a fast: `fast resume`
- Check fasting status: `fast status`
- View fasting history: `fast history`

Additional options:

- Start a fast with initial duration: `fast start --duration HH:MM`
- Stop a fast without saving it: `fast stop --discard`
- View limited number of history entries: `fast history --limit N`

## Examples

1. Start a new fast:
   ```
   fast start
   ```

2. Start a fast, indicating you've already been fasting for 2 hours and 30 minutes:
   ```
   fast start --duration 02:30
   ```

3. Check your current fasting status:
   ```
   fast status
   ```

4. Pause your current fast:
   ```
   fast pause
   ```

5. Resume your paused fast:
   ```
   fast resume
   ```

6. Stop your current fast and save it:
   ```
   fast stop
   ```

7. Stop your current fast without saving it:
   ```
   fast stop --discard
   ```

8. View your fasting history:
   ```
   fast history
   ```

9. View your last 5 fasts:
   ```
   fast history --limit 5
   ```

## Data Storage

Your fasting data is stored in the following locations:

- Current fasting state: `~/.fasting_tracker/fasting_tracker_data.json`
- Completed fasts: `~/.fasting_tracker/completed_fasts.json`
- Log file (for troubleshooting): `~/.fasting_tracker_log.txt`

## Contributing

Contributions to improve Fast CLI are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any problems or have any questions, please file an issue on the GitHub repository.

Happy fasting!# Fast CLI

Fast CLI is a simple command-line interface tool to help you track your fasting schedules. It allows you to start, stop, pause, and resume fasting timers, as well as check your current fasting status and view your fasting history.

## Features

- Start a fasting timer
- Stop a fasting timer (with option to store or discard the fast)
- Pause and resume fasting timers
- Check current fasting status
- Store completed fasts for later review
- Start a timer with a specific initial duration
- View history of completed fasts

## Installation

1. Ensure you have Python 3.7 or later installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/fast-cli.git
   cd fast-cli
   ```

3. Install the package:
   ```
   pip install -e .
   ```

## Usage

After installation, you can use the `fast` command from anywhere in your terminal.

Basic commands:

- Start a fast: `fast start`
- Stop a fast: `fast stop`
- Pause a fast: `fast pause`
- Resume a fast: `fast resume`
- Check fasting status: `fast status`
- View fasting history: `fast history`

Additional options:

- Start a fast with initial duration: `fast start --duration HH:MM`
- Stop a fast without saving it: `fast stop --discard`
- View limited number of history entries: `fast history --limit N`

## Examples

1. Start a new fast:
   ```
   fast start
   ```

2. Start a fast, indicating you've already been fasting for 2 hours and 30 minutes:
   ```
   fast start --duration 02:30
   ```

3. Check your current fasting status:
   ```
   fast status
   ```

4. Pause your current fast:
   ```
   fast pause
   ```

5. Resume your paused fast:
   ```
   fast resume
   ```

6. Stop your current fast and save it:
   ```
   fast stop
   ```

7. Stop your current fast without saving it:
   ```
   fast stop --discard
   ```

8. View your fasting history:
   ```
   fast history
   ```

9. View your last 5 fasts:
   ```
   fast history --limit 5
   ```

## Data Storage

Your fasting data is stored in the following locations:

- Current fasting state: `~/.fasting_tracker/fasting_tracker_data.json`
- Completed fasts: `~/.fasting_tracker/completed_fasts.json`
- Log file (for troubleshooting): `~/.fasting_tracker_log.txt`