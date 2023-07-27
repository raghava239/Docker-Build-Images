from flask import Flask
app = Flask(__name__)

@app.route('/')
def hell_world():
    return 'Hello World , This is my Application'
if __name__ == '__main__':
    app.run()