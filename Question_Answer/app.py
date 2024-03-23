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
    db=get_db()
    if current_user is None:
        return redirect(url_for('login'))
    question_cur = db.execute('select questions.id as id,questions.question_test as question,askers.user_name as asker_name,experts.user_name as expert_name from questions join users as askers on askers.id = questions.asked_by_id join users as experts on  experts.id = questions.expert_id where answer_text is not null')
    question_res = question_cur.fetchall()
    return render_template('home.html',user = current_user,question_home = question_res)

@app.route('/register',methods=['GET','POST'])
def register():
    db = get_db()

    current_user = get_current_user()

    # hashing the passowrd
    if request.method == 'POST':
        name =  request.form['Name']

        current_user_cur = db.execute('select user_name from users where user_name=? ',[name])
        current_user_res = current_user_cur.fetchone()
        if current_user_res:
            return render_template('register.html',user = current_user,error = 'User Already Exist')

        hashed_password =  generate_password_hash(request.form['Password'],method='pbkdf2:sha256')
        db.execute('insert into users(user_name,password,expert,admin) \
            values (?,?,?,?)',[name,hashed_password,'0','0'])
        db.commit()
        session['user'] = name
        return redirect(url_for('index'))
       
    return render_template('register.html',user = current_user)

@app.route('/login',methods=['GET','POST'])
def login():
    db = get_db()
    error = None
    current_user = get_current_user()

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        cu = db.execute('select * from users where user_name = ? '\
            ,[name])

        rec = cu.fetchone()

        if rec:
            if check_password_hash(rec['password'],password):
                session['user'] = name
                return redirect(url_for('index'))
            else:
                error = 'Passoword incorrect!....'
        else:
            error= 'User not Present!....'
        return render_template('login.html',error = error)
    return render_template('login.html')

@app.route('/question/<question_id>')
def question(question_id):
    current_user = get_current_user()
    if current_user is None:
        return redirect(url_for('login'))
    db = get_db()
    question_cur = db.execute('select questions.id as id,questions.answer_text as answer_text,questions.question_test as question,askers.user_name as asker_name,experts.user_name as expert_name from questions join users as askers on askers.id = questions.asked_by_id join users as experts on  experts.id = questions.expert_id where questions.id=?',[question_id])
    questions = question_cur.fetchone()
    return render_template('question.html',user = current_user,questions_details = questions)

@app.route('/answer/<question_id>',methods = ['GET','POST'])
def answer(question_id):
    current_user = get_current_user()

    if not current_user:
        return redirect(url_for('login'))


    if current_user['expert'] != 1:
        return redirect(url_for('index'))

    db = get_db()
    if request.method =='POST': 
        answer_res = request.form['answer']
        db.execute('update questions set answer_text = ? where id  = ?',[answer_res,question_id])
        db.commit()

        return redirect(url_for('unanswered'))

    question_cur = db.execute('select * from questions where id = ?',[question_id])    
    question_is = question_cur.fetchone()
    return render_template('answer.html',user = current_user,actual_question=question_is)

@app.route('/ask',methods =['POST','GET'])
def ask():
    current_user = get_current_user()

    if not current_user:
        return redirect(url_for('login'))

    db = get_db()

    if request.method =='POST':
        question_text = request.form['question']
        expert_id = request.form['expert']
        asked_by_id = current_user['id']

        db.execute('insert into questions(question_test,expert_id,asked_by_id) values(?,?,?)',\
                        [question_text,expert_id,asked_by_id])
        db.commit()
        return redirect(url_for('index'))

    expert_cur = db.execute('select * from users where expert = 1')
    expert_users = expert_cur.fetchall()

    return render_template('ask.html',user = current_user,expert_users = expert_users )

@app.route('/unanswered')
def unanswered():
    current_user = get_current_user()

    if not current_user:
        return redirect(url_for('login'))

    if current_user['expert'] != 1:
        return redirect(url_for('index'))

    db = get_db()
    question_cur = db.execute('select questions.id as id,users.user_name as asked_user,questions.question_test as question_of_user from questions join users on questions.asked_by_id = users.id where questions.expert_id = ? and questions.answer_text is null',[current_user['id']])
    all_questions = question_cur.fetchall()

    return render_template('unanswered.html',user = current_user,questions = all_questions)

@app.route('/users')
def users():
    current_user = get_current_user()
    if not current_user:
        return redirect(url_for('login'))

    if current_user['admin'] != 1:
        return redirect(url_for('index'))

    db = get_db()
    user_cur = db.execute('select id,user_name,expert,admin from users')
    user_res = user_cur.fetchall()

    return render_template('users.html',user = current_user,all_users=user_res)

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))


@app.route('/promote/<user_id>')
def promote(user_id):
    current_user = get_current_user()

    if not current_user:
        return redirect(url_for('login'))

    if current_user['admin'] != 1:
        return redirect(url_for('index'))

    db = get_db()
    db.execute('update users set expert = 1 where id = ?',[user_id])
    db.commit()
    return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(debug=True)
