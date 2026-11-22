def calculate(a, b, operation):
	if operation == "+":
		return a + b
	if operation == "-":
		return a - b
	if operation == "*":
		return a * b
	if operation == "/":
		if b == 0:
			raise ValueError("Cannot divide by zero")
		return a / b
	raise ValueError("Unknown operation")


if __name__ == "__main__":
	first = float(input("First number: "))
	operation = input("Operation (+, -, *, /): ")
	second = float(input("Second number: "))
	print("Result:", calculate(first, second, operation))
