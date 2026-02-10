from flask import Flask, request, render_template_string

app = Flask(__name__)

# This is the "Face" of your app (HTML)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Engineer's Calculator</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; padding-top: 50px; background-color: #f4f4f9; }
        .card { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input { padding: 10px; margin: 5px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; background-color: #2ecc71; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>God-centered Engineer Calculator</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" placeholder="First Number" required>
            <span> + </span>
            <input type="number" step="any" name="num2" placeholder="Second Number" required>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <h3>Result: {{ result }}</h3>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # Taking the inputs from the form
        a = float(request.form.get('num1'))
        b = float(request.form.get('num2'))
        result = a + b

    # Sending the HTML back to the browser
    return render_template_string(HTML_TEMPLATE, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)