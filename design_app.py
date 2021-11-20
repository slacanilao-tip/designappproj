from flask import Flask, render_template, request

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("login.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)