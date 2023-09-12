from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Soumya</h1>"

if __name__ == "__main__":
    app.run(port=5500)