from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running!"

@app.route('/hang')
def hang():
    global stop_responding
    stop_responding = True
    return "App will stop responding!"

stop_responding = False

@app.route('/healthz')
def healthz():
    if stop_responding:
        time.sleep(1000)  # Simulate a hang (never returns response)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
