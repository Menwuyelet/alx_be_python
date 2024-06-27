task = input ("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
  case "high":
    if time_bound == "yes":
       reminder = f"'{task}' is a high priority task that requires immediate attention today!"
       print("Reminder:", reminder)  
    elif time_bound == "no":
       reminder = f"'{task}' is a high priority task. but it is not time bounded."
       print("Note:", reminder)
  case "medium":
    if time_bound == "yes":
      reminder = f"'{task}' is a medium priority task, but it is time bounded."
      print("Reminder:", reminder)
    elif time_bound == "no":
      reminder = f"'{task}' is a medium priority task and it is not time bounded."
      print("Note:", reminder)
  case "low":
    if time_bound == "yes":
      reminder = f"'{task}' is a low priority task, but it is time bounded."
      print("Note:", reminder)
    elif time_bound == "no":
      reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
      print("Note:", reminder)

