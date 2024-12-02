from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

# Define the HTML content directly inside app.py as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Add your CSS here directly or keep it in a separate file */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            text-align: center;
            padding: 50px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        input, select, button {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            box-sizing: border-box;
            font-size: 16px;
        }
        .result {
            margin-top: 20px;
            font-size: 20px;
        }
        .error {
            color: red;
        }
    </style>
    <title>Simple Calculator</title>
</head>
<body>
    <div class="container">
        <h1>Simple Calculator</h1>
        <form method="POST">
            <input type="text" name="num1" placeholder="Enter first number" required>
            <input type="text" name="num2" placeholder="Enter second number" required>
            <select name="operation" required>
                <option value="add">Addition</option>
                <option value="subtract">Subtraction</option>
                <option value="multiply">Multiplication</option>
                <option value="divide">Division</option>
                <option value="power">Power</option>
                <option value="sqrt">Square Root</option>
                <option value="modulus">Modulus</option>
                <option value="log">Logarithm</option>
                <option value="factorial">Factorial</option>
                <option value="exp">Exponential</option>
                <option value="sin">Sine</option>
                <option value="cos">Cosine</option>
                <option value="tan">Tangent</option>
                <option value="average">Average</option>
                <option value="percentage">Percentage</option>
                <option value="cgpa">CGPA</option>
            </select>
            <button type="submit">Calculate</button>
        </form>
        
        {% if result is not none %}
        <div class="result">
            <h2>Result: {{ result }}</h2>
        </div>
        {% endif %}
        
        {% if error_message %}
        <div class="error">
            <h2>{{ error_message }}</h2>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


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

    return render_template_string(
        html_content, result=result, error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)
