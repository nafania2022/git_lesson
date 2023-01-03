from flask import Flask
app = Flask(__name__)

# @app.route('/')
def hello_world():
    return 'Hello World!'

app.add_url_rule("/", view_func=hello_world)

app.run()