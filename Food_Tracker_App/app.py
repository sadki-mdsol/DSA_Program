from flask import Flask,render_template,request,g
from datetime import datetime
from database import get_db


app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite3_db'):
        g.sqlite3_db.close()


@app.route('/',methods =['GET','POST'])
def home():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        datetime_obj = datetime.strptime(date,'%Y-%m-%d')
        final_db_date = datetime.strftime(datetime_obj,'%Y%m%d')
        
        db.execute('insert into log_data(entry_date) values(?)',[final_db_date])
        db.commit()
    cur = db.execute('select log_data.entry_date as entry_date, sum(food.protein) as protein_sum, \
            sum(food.carbohydrates) as carbs_sum,\
                 sum(food.fat) as fat_sum,\
                     sum(food.calories) as cal_sum \
            from log_data left join food_date on food_date.log_date_id = log_data.id  \
            left join food on food.id = food_date.food_id group by log_data.entry_date \
            order by log_data.entry_date desc')
    result = cur.fetchall()
    date_result = []
    for i in range(0,len(result)):
        dates_value = {}

        date = str(result[i]['entry_date'])
        date_time_ob = datetime.strptime(date,'%Y%m%d')

        dates_value['entry_date'] = datetime.strftime(date_time_ob,'%B %d, %y')
        dates_value['date'] = result[i]['entry_date']
        dates_value['protein_sum'] = result[i]['protein_sum']
        dates_value['carbs_sum'] = result[i]['carbs_sum']
        dates_value['fat_sum'] = result[i]['fat_sum']
        dates_value['cal_sum'] = result[i]['cal_sum']
        date_result.append(dates_value)

    

    return render_template('home.html',dates = date_result)

@app.route('/food',methods=['GET','POST'])
def food():
    db = get_db()
    if request.method =='POST':
        name = request.form['name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        
        calories = protein * 4 + carbohydrates * 4 + fat * 9
        db.execute('insert into food\
                    (food_name ,protein,carbohydrates,fat,calories )\
                    values (?,?,?,?,?)',\
                    [name,protein,carbohydrates,fat,calories])
        db.commit()
    cur = db.execute('select  * from food')
    result = cur.fetchall()
    return render_template('add_food.html',food_items = result)

@app.route('/view/<date>',methods = ['GET','POST'])
def view(date):
    db = get_db()
    cur = db.execute('select entry_date,id from log_data where entry_date = ?',[date])
    result = cur.fetchone()
    if request.method == 'POST':
        food_id = request.form['food_selected']
        date_id = result['id']

        db.execute('insert into food_date(food_id,log_date_id) \
                                        values (?,?)'\
                                    ,[food_id,date_id])
        db.commit()


    database_date = datetime.strptime(str(result['entry_date']),'%Y%m%d')
    date_display = datetime.strftime(database_date, '%B %d, %y')
    food_cur = db.execute('select id,food_name from food')
    all_foods = food_cur.fetchall()


    log_curr = db.execute('select food.food_name,food.protein, food.carbohydrates, food.fat, food.calories from log_data join food_date on food_date.log_date_id = log_data.id join food on food.id = food_date.food_id  where log_data.entry_date = ? ',[date])
    log_result = log_curr.fetchall()

    total = {'protein':0,'fat':0,'carbohydrates':0,'calories':0}
    for each in log_result:
        total['protein'] += each['protein']
        total['fat'] += each['fat']
        total['carbohydrates'] += each['carbohydrates']
        total['calories'] += each['calories']

    return render_template('day.html',entry_date = result['entry_date'],preety_date = date_display, foods = all_foods,log_results =log_result,total_fats = total)

if __name__ == '__main__':
    app.run(debug=True)

