import signal
import sys
from .race import Race


def handle_exit_signal(signum, frame):
    """
    Handles the CTRL+C signal to cleanly exit the program.
    """
    print("\nExiting program...")
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, handle_exit_signal)


def main(argv):
    # Default parameters
    num_runners = 4
    track_size = 700

    race = Race(num_runners, track_size)
    race.start()


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        handle_exit_signal(None, None)
