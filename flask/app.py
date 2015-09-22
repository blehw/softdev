from flask import Flask

app = Flask(__name__)

#When someone goes to "/home", do the thing (must return string).
@app.route("/home")
def home():
    return "<h1>Wazzzupppp???</h1>"

#Debug is true to get better error messages
#Run the app. The host COULD be IP address, but normally put it down as 0.0.0.0 so that anyone can use the app.
if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8000)
