from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = ""
    if request.method == 'POST':
        try:
            # Get numbers and operation from the form
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error: Division by Zero"
        except Exception as e:
            result = "Invalid Input"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)