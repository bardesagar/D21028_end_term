from flask import Flask

app = Flask(__name__) #constructor of the flask

@app.route('/<name>')
def base_route(name):
    return f"welcome {name}"


if __name__ == "__main__":
    app.run()