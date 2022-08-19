from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)
@app.route('/')
def schedule():
    return render_template('schedule.html', id = id)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
