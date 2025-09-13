import time
import os


def countdown_timer(time_in_seconds: int):
    """Display a countdown timer in HH:MM:SS format."""
    for x in range(time_in_seconds, -1, -1):
        hours = x // 3600
        minutes = x % 3600 // 60
        seconds = x % 60
        if x >= 0:
            os.system("cls" if os.name == "nt" else "clear")
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)


def get_time_in_seconds() -> int:
    """Prompt the user for a countdown time in seconds and validate input."""
    while True:
        try:
            time_in_seconds = int(input("Enter the time in seconds: "))
            if time_in_seconds <= 0:
                print("⚠ The time must be greater than 0.")
                continue
            return time_in_seconds
        except ValueError:
            print("⚠ The time must be an integer.")


def main():
    """Main loop for the countdown timer application."""
    print("-----------------------")
    print("WELCOME TO THE COUNTDOWN TIMER")
    print("-----------------------")
    try:
        while True:
            time_in_seconds = get_time_in_seconds()
            print("-----------------------")
            countdown_timer(time_in_seconds)
            print("-----------------------")
            want_exit = input("Do you want to exit? (Y/N): ").strip().lower()
            if want_exit in ("y", "yes"):
                print(
                    "Thank you for using the app\nMade with love by Majed Abumathkour"
                )
                break
    except KeyboardInterrupt:
        print("\nExiting gracefully. Goodbye!")


if __name__ == "__main__":
    main()
