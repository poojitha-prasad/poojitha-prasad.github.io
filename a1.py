from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return '<h1>hello</h1>'


if __name__=="__main__":
   app.run(debug(True))
