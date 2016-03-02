from flask import Flask,render_template
from FlaskApp.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello There! You</h1>"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


