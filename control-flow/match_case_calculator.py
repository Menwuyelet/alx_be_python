num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
  case "+":
    result = num1 + num2
    print("The result is " + str(result)+".")
  case "-":
    result = num1 - num2
    print("The result is " + str(result)+".")
  case "*":
    result = num1 * num2
    print("The result is " + str(result)+".")
  case "/":
    if num2 != 0:
      result = num1 / num2
      print("The result is " + str(result)+".")
    elif num2 == 0:
      print("Cannot divide by zero.")


