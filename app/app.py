from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form["text"]
        with open('Failed.py', 'w') as file_:
            file_.write(code)
        return render_template('index.html', code=code)
    elif request.method == 'GET':
        return render_template('index.html', code="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
