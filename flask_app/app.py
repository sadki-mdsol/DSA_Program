from flask import Flask,jsonify,request

app = Flask(__name__)

# @app.route('/<name>')
# def index_name(name):
#     return '<h1>Hello {}!</h1>'.format(name)


@app.route('/')
def index():
    return '<h1>Hello World !</h1>'

#set default value to /home
@app.route('/home',methods = ['POST','GET'],defaults={'name':'Default'})

#seperate route with the name as route variable
@app.route('/home/<name>',methods = ['POST','GET'])


#bind type to /home/<int:name> <string:name>
@app.route('/home/<int:name>',methods = ['POST','GET'])
def home_page(name):
    return '<h1>{} are at home page!.....</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key':'val1','list_key':[1,2,3,]})

#handle query in route (& and ?)
@app.route('/query',methods=['POST','GET'])
def get_query():
    name = request.args.get('name')
    location = request.args.get('location')
    return jsonify({'name':name , 'location':location})

#create a form & send to process route to display details of form
@app.route('/form')
def get_details_form():
    return '''
        <form action='/process' method='POST'>
            <input type='text' name='name'><br>
            <input type='text' name='location'><br>
            <input type='submit' value='Submit'>
        </from>
    '''

@app.route('/process' , methods=['POST'])
def disply_details():
    name = request.form['name']
    location = request.form['location']
    return '''<h1>
        {} is at location {}</h1>
        '''.format(name,location)

#get the data from json for POST req
@app.route('/processjson',methods = ['POST'])
def process_json_post():
    data = request.get_json()
    name = data['name']
    location = data['location']
    languages = data['languages']

    return jsonify({'result':'Success!...','name':name,'location':location,'first_language':languages[1],'Languages known':languages,'complete_data':data})

if __name__ == '__main__':
    app.run(debug=True)