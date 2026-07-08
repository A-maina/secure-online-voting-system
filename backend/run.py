from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Secure Online Voting API is running",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    app.run(debug=True)