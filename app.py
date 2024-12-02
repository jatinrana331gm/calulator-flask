from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error_message = None

    if request.method == "POST":
        try:
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            operation = request.form["operation"]

            if (
                not num1.replace(".", "", 1).isdigit()
                or not num2.replace(".", "", 1).isdigit()
            ):
                raise ValueError("Invalid input! Please enter valid numbers.")

            num1 = float(num1)
            num2 = float(num2)

            # Perform operations
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Error! Division by zero."
                else:
                    result = num1 / num2
            elif operation == "power":
                result = math.pow(num1, num2)
            elif operation == "sqrt":
                if num1 < 0:
                    result = "Error! Square root of a negative number."
                else:
                    result = math.sqrt(num1)
            elif operation == "modulus":
                result = num1 % num2
            elif operation == "log":
                if num1 <= 0:
                    result = "Error! Logarithm of non-positive numbers is not possible."
                else:
                    result = math.log(num1)
            elif operation == "factorial":
                if num1 < 0 or int(num1) != num1:
                    result = "Error! Factorial of negative or non-integer numbers is not possible."
                else:
                    result = math.factorial(int(num1))
            elif operation == "exp":
                result = math.exp(num1)
            elif operation == "sin":
                result = math.sin(math.radians(num1))
            elif operation == "cos":
                result = math.cos(math.radians(num1))
            elif operation == "tan":
                result = math.tan(math.radians(num1))
            elif operation == "average":
                result = (num1 + num2) / 2
            elif operation == "percentage":
                result = (num1 / num2) * 100
            elif operation == "cgpa":
                result = (num1 + num2) / 2  # Basic average for CGPA
            else:
                result = "Unknown operation!"
        except ValueError as e:
            error_message = str(e)
        except Exception as e:
            error_message = "An unexpected error occurred: " + str(e)

    return render_template("calculator.html", result=result, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
