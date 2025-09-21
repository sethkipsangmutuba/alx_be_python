#!/usr/bin/env python3
# daily_reminder.py
# Provides a customized reminder for a single daily task

def main():
    # Prompt for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case to handle priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unknown priority level"

    # Add time sensitivity check
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message = "Note: " + message + ". Consider completing it when you have free time."

    # Output final reminder
    print("\nReminder:", message)


if __name__ == "__main__":
    main()
