from datetime import datetime, timedelta

def get_time_input(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%H:%M:%S")
        except ValueError:
            print("Invalid format! Please enter time in HH:MM:SS format.")

def get_duration_input(prompt):
    while True:
        try:
            h, m, s = map(int, input(prompt).split(":"))
            return timedelta(hours=h, minutes=m, seconds=s)
        except:
            print("Invalid format! Please enter duration in HH:MM:SS format.")

# Step 1: Get actual meeting start time
print("=== Actual Meeting Time Calculator ===")
meeting_start = get_time_input("Enter actual meeting start time (HH:MM:SS): ")

# Step 2: (Optional) Get total call duration
call_duration = get_duration_input("Enter total call duration (HH:MM:SS): ")

while True:
    # Step 3: Enter playback time
    playback_duration = get_duration_input("\nEnter playback timestamp (HH:MM:SS): ")

    if playback_duration > call_duration:
        print("⚠️  Playback time exceeds meeting duration. Try again.")
        continue

    # Step 4: Calculate actual time
    actual_time = (datetime.combine(datetime.today(), meeting_start.time()) + playback_duration).time()
    print(f"🕒 Actual time during the meeting: {actual_time}")

    # Continue?
    cont = input("Do you want to check another playback time? (y/n): ").strip().lower()
    if cont != 'y':
        print("✅ Done. Thank you!")
        break
