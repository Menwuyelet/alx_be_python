task = input ("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high" and time_bound == "yes":
  print(f"'{task}' is a high priority task that requires immediate attention today!")
elif priority == "medium" and time_bound == "yes":
  print(f"'{task}' is a medium priority task, but it is time bounded.")
elif priority == "low" and time_bound == "yes":
  print(f"'{task}' is a low priority task, but it is time bounded.")
elif priority == "high" and time_bound == "no":
  print(f"'{task}' is a high priority task. but it is not time bounded.")
elif priority == "medium" and time_bound == "no":
  print(f"'{task}' is a medium priority task and it is not time bounded.")
elif priority == "low" and time_bound == "no":
  print(f"'{task}' is a low priority task. Consider completing it when you have free time.")