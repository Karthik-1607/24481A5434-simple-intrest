from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/greet/<uname>')
def greet(uname):
    return f"Hello, {uname}! This system provides information and resources related to AIDS awareness."

@app.route('/calculate', methods=['GET', 'POST'])
def simple_interest():
    result = None

    if request.method == 'POST':
        try:
            principal = float(request.form.get('principal', 0))
            rate = float(request.form.get('rate', 0))
            time = float(request.form.get('time', 0))
            result = (principal * rate * time) / 100
        except ValueError:
            result = None

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=3500)
