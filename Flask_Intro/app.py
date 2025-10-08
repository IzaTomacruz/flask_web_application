from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_circle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', '').strip())
            if radius < 0:
                result = "Radius cannot be negative."
            else:
                result = round(3.14159 * (radius ** 2), 4)
        except ValueError:
            result = "Invalid input. Please enter a number."
    return render_template('area_circle.html', result=result)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def area_triangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', '').strip())
            height = float(request.form.get('height', '').strip())

            if base < 0 or height < 0:
                result = "Base and height must be positive numbers."
            else:
                result = round(0.5 * base * height, 4)
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('area_triangle.html', result=result)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/contacts')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
