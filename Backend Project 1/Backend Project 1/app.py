from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    matches = []
    error = ""

    if request.method == 'POST':

        text = request.form['text']
        pattern = request.form['pattern']

        try:
            matches = re.findall(pattern, text)

            if not matches:
                error = "No matches found!"

        except re.error:
            error = "Invalid Regular Expression!"


    return render_template('index.html', matches=matches, error=error)


if __name__ == '__main__':
    app.run(debug=True)