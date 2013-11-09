from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> This app is running! </h1><p>Hi Glenn</p>"

if __name__ == '__main__':
    app.run(port=8000)
