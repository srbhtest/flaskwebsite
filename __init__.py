from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello There! You</h1>"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


