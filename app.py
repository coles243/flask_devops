from flask import Flask,render_template
from datetime import datetime
import os
app=Flask(__name__)

@app.route("/")
def index():
    time=datetime.now()
    return render_template("index.html", time=time)


if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0",port=port)