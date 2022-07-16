from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
  return {
    "status": 200,
    "msg": "Active!!"
  }

if __name__ == "__main__":
  app.run(debug=True)