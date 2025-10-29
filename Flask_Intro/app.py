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

@app.route('/works')
def works():
    return render_template('works.html')

# Infix to Postfix Conversion

def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

def infix_postfix(expression):
    ops = [] #stack for operators
    output = [] #stack for output
    
    for token in expression:
        #if token is an Operand, add to output stack
        if token.isalnum():
            output.append(token)
        #if token is an open bracket "(", push it onto ops stack
        elif token == '(':
            ops.append(token)
        #if token is a closing bracket ")", while top of ops is not '(', pop the ops and push to the output
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            ops.pop()
        #if token is an operator, 
        elif token in ['+', '-', '*', '/', '^']:
            while ops and precedence(ops[-1]) >= precedence(token):
                output.append(ops.pop())    
            ops.append(token)
            
    while ops:
        output.append(ops.pop())

    return output

@app.route('/infix_to_postfix', methods=['GET', 'POST'])
def infix_to_postfix():
    result = None
    if request.method == 'POST':
        infix_expression = request.form.get('expression', '').strip()
        postfix_expression = infix_postfix(infix_expression)
        result = ' '.join(postfix_expression)
    return render_template('infix_to_postfix.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
