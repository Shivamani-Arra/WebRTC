from flask import Flask,url_for,redirect,request,render_template
app=Flask(__name__,template_folder='templates')
@app.route('/')
def Drone():
   return render_template("drone.html")
@app.route('/success/<name>')
def success(name):
    return "Successfull Logined %s " % name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)