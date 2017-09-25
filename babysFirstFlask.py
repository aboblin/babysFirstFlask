from flask import Flask

babys_app = Flask(__name__)

@babys_app.route("/")
def root():
    return "<center><h1>Quiz Your Friends!</h1></center>"

@babys_app.route("/incorrect")
def incorrect():
    return "try again tomorrow so sad~!"

@babys_app.route("/correct")
def correct():
    return "yes :) you are right"

@babys_app.route("/hidden")
def hidden():
    return "oooo you found the hidden page"

if __name__ == "__main__":
    babys_app.debug = True
    babys_app.run()
