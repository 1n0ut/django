from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/show/info")
def inidex():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/get/reg")
def do_register():
    print(request.args)
    return "pass"

@app.route("/post/reg",methods=['post'])
def post_register():
    print(request.form)
    return "pass"

if __name__=="__main__":
    app.run()