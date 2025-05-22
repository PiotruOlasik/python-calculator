# main.py
from flask import Flask, render_template, request
app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "add":
                result = add(a, b)
            elif operation == "subtract":
                result = subtract(a, b)
            elif operation == "multiply":
                result = multiply(a, b)
            elif operation == "divide":
                result = divide(a, b)
            else:
                error = "Nieznana operacja"
        except ValueError as ve:
            error = str(ve)
        except Exception:
            error = "Błąd danych wejściowych"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
