from flask import Flask,jsonify,g,request
from database import get_db
from functools import wraps
import json

app = Flask(__name__)

api_username = 'admin'
api_password = 'password'

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args, **kwargs)
        else:
            return jsonify({'message':'Authetictaion Failed!.....'}),403
    return decorated

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite3_db'):
        g.sqlite3_db.close()

@app.route('/members',methods = ['GET'])
@protected
def get_members():
    db = get_db()
    member_all_cur = db.execute('select * from members')
    member_res = member_all_cur.fetchall()

    final_res = []
    for member in member_res:
        member_dict = {}
        member_dict['id'] = member['id']
        member_dict['member_name'] = member['member_name']
        member_dict['email'] = member['email']
        member_dict['member_level'] = member['member_level']
        final_res.append(member_dict)

    return jsonify({'user_details':final_res})
    
@app.route('/members/<int:member_id>',methods = ['GET'])
@protected
def enter_member(member_id):
    db = get_db()
    member_all_cur = db.execute('select * from members where id = ?',[member_id])
    member_res = member_all_cur.fetchone()
    final_res = []
    member_dict={}
    member_dict['id'] = member_res['id']
    member_dict['member_name'] = member_res['member_name']
    member_dict['email'] = member_res['email']
    member_dict['member_level'] = member_res['member_level']
    final_res.append(member_dict)

    return jsonify({'user_details':final_res})

@app.route('/members',methods = ['POST'])
@protected
def add_members():
    member_details = request.get_json()
    name = member_details['name']
    email = member_details['email']
    level = member_details['level']
    db = get_db()
    db.execute('insert into members(member_name,email,member_level) values(?,?,?)',[name,email,level])
    db.commit()

    mem_cur = db.execute('select * from members where member_name= ?',[name])
    mem_res = mem_cur.fetchone()

    return jsonify({'user_details': {'id':mem_res['id'],
                    'name':mem_res['member_name'],
                    'email':mem_res['email'],
                    'member_level':mem_res['member_level']}})


@app.route('/members/<int:member_id>',methods = ['PUT','PATCH'])
@protected
def edit_members(member_id):
    new_member_details = request.get_json()
    name = new_member_details['name']
    email = new_member_details['email']
    level = new_member_details['level']

    db = get_db()
    db.execute('update members set member_name = ?, email = ?,member_level = ? where id = ?',[name,email,level,member_id])
    db.commit()

    updated_mem_cur = db.execute('select * from members where id = ?',[member_id])
    updated_mem_res = updated_mem_cur.fetchone()

    final_updated_dict = []
    sinle_dict = {}
    sinle_dict['member_name']=updated_mem_res['member_name']
    sinle_dict['email']=updated_mem_res['email']
    sinle_dict['member_level']=updated_mem_res['member_level']
    final_updated_dict.append(sinle_dict)


    return jsonify({'user_details':final_updated_dict})

@app.route('/members/<int:member_id>',methods = ['DELETE'])
@protected
def delete_members(member_id):
    db = get_db()
    db.execute('delete from members where id = ? ',[member_id])
    db.commit()

    return jsonify({'status':'Member has been deleted!..'})


if __name__ == '__main__':
    app.run(debug=True)