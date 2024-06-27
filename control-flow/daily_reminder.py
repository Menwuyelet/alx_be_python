task = input ("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
  case "high":
    if time_bound == "yes":
       print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")  
    elif time_bound == "no":
       print(f"Note: '{task}' is a high priority task. but it is not time bounded.")
  case "medium":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a medium priority task, but it is time bounded.")
    elif time_bound == "no":
      print(f"Note: '{task}' is a medium priority task and it is not time bounded.")
  case "low":
    if time_bound == "yes":
      print(f"Note: '{task}' is a low priority task, but it is time bounded.")
    elif time_bound == "no":
      print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

