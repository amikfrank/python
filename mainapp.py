from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
   response = {"message":"Hello from New World! This has been a long day"}
   return jsonify(response)

if __name__ == "__main__":
   app.run(host='0.0.0.0')
