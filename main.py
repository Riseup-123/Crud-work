from flask import Flask,render_template,request,redirect,url_for,session,send_file,jsonify
from DBConnection import Db

app = Flask(__name__)


######## Create user function ##############

@app.route('/user_add',methods=['post'])
def user_add():
    db1 = Db()
    try:
        username=request.form['username']
	password=request.form['password']
	active=request.form['active']

        qry1="INSERT INTO users_table(username,password,state)VALUES('"+username+"','"+password+"','"+active+"')"
        res=db1.insert(qry1)
        if int(res)>0:
            return '<script>alert("Successfully addded...");window.location="some home page"</script>'
        else:
            return '<script>alert("error");window.location="some home page"</script>'
    except Exception as e:
        print(str(e))

######## View users function ##############

@app.route('/view_users')
def view_users():
    db = Db()
    qry = "SELECT * FROM users_table"
    res = db.select(qry)
    if len(res) > 0:
        return render_template("some html page.html", result=res)
    else:
        return '<script>alert("No data....");window.location="some home page"</script>'

######## Remove user function ##############

@app.route('/remove_user/<uid>')
def remove_user(uid):
    db = Db()
    qry = "DELETE FROM users_table WHERE uid='"+uid+"'"
    res = db.delete(qry)
    if res>0:
        return '<script>alert("Successfully deleted.........");window.location="user view section"</script>'
    else:
        return '<script>alert("Error....");window.location="some home page"</script>'

######## Update user function ##############

@app.route('/user_update',methods=['post'])
def user_update():
    db1 = Db()
    try:
        username = request.form['username']
        password = request.form['password']
	active = request.form['active']
        uid = request.form['uid']

        qry1="UPDATE users_table SET username='"+username+"',password='"+password+"',state='"+active+"' WHERE uid='"+uid+"'"
        res=db1.update(qry1)

        return '<script>alert("Successfully updated...");window.location="user view section"</script>'

    except Exception as e:
        print(str(e))



######## end of function ##############

if __name__ == '__main__':
    app.run()
