from flask import Flask
import webbrowser

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
