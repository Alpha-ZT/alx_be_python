from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    try:
        days_input = input("Enter the number of days to add to the current date: ").strip()
        days = int(days_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return

    calculate_future_date(days)

if __name__ == "__main__":
    main()
