from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/myapi", methods = ['GET'])
def hello():
    d = {}
    path = str(request.args['image'])
    output = util.classify(path)
    d["class"] = output
    return d

if __name__ == "__main__":
    app.run(port=5500)