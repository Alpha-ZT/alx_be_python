# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate message based on priority and time-bound
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please schedule it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to get to it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but it's time-bound. Try to finish it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use 'high', 'medium', or 'low'.")
