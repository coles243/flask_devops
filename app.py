from flask import Flask,render_template
from datetime import datetime
app=Flask(__name__)

@app.route("/")
def index():
    time=datetime.now()
    return render_template("index.html", time=time)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=3000)