from flask import Flask,render_template,g,request,session,redirect,url_for
from databse import get_db
from werkzeug.security import check_password_hash,generate_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite3_db'):
        g.sqlite3_db.close()

def get_current_user():
    user_result = None
    if 'user' in session:
        user = session['user']
        db = get_db()
        user_cur = db.execute('select * from users where user_name = ?',[user])
        user_result = user_cur.fetchone()
    return user_result

@app.route('/')
def index():
    current_user = get_current_user()

    return render_template('home.html',user = current_user)

@app.route('/register',methods=['GET','POST'])
def register():
    db = get_db()

    current_user = get_current_user()

    # hashing the passowrd
    if request.method == 'POST':
        name =  request.form['Name']
        hashed_password =  generate_password_hash(request.form['Password'],method='pbkdf2:sha256')
        db.execute('insert into users(user_name,password,expert,admin) \
            values (?,?,?,?)',[name,hashed_password,'0','0'])
        db.commit()
    return render_template('register.html',user = current_user)

@app.route('/login',methods=['GET','POST'])
def login():
    db = get_db()

    current_user = get_current_user()

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        cu = db.execute('select * from users where user_name = ? '\
            ,[name])

        rec = cu.fetchone()
        if check_password_hash(rec['password'],password):
            session['user'] = name
            # return render_template('home.html')
            return 'Login successful'
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/question')
def question():
    current_user = get_current_user()
    return render_template('question.html',user = current_user)

@app.route('/answer')
def answer():
    current_user = get_current_user()
    return render_template('answer.html',user = current_user)

@app.route('/ask')
def ask():
    current_user = get_current_user()
    return render_template('ask.html',user = current_user)

@app.route('/unanswered')
def unanswered():
    current_user = get_current_user()
    return render_template('unanswered.html',user = current_user)

@app.route('/users')
def users():
    current_user = get_current_user()
    return render_template('users.html',user = current_user)

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

