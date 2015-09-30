from flask import Flask, render_template, request
import utils

app = Flask(__name__)

#When somxeone goes to "/home", do the thing (must return string).
@app.route("/index",methods=["get","post"])
@app.route("/",methods=["get","post"])
def index():
    #print request.args
    #return render_template("index.html",args=request.args)
    #if request.method=="post":
    #   return render_template("index.html")
    #else:
        uname=request.form['username']
        pword=request.form['password']
        if button=="cancel":
            return render_template("index.html")
        if utils.authenticate(uname,pword):
            return "You're in"
        else:
            return render_template("login.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
