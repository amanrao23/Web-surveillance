from flask import Flask,render_template,request,send_file,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import getinfoform
from datetime import datetime
from sqlalchemy import and_
app=Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class Video(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    start_time=db.Column(db.Integer)
    end_time=db.Column(db.Integer)
    filepath=db.Column(db.String)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/go',methods=['GET','POST'])
def go():
    form=getinfoform()
    if form.is_submitted():
        a=form.startime.data
        b=form.endtime.data
        qry1=Video.query.filter(Video.start_time <= a,Video.end_time >= b)
        qry2=Video.query.filter(Video.start_time >= a,Video.start_time <= b)
        qry3=Video.query.filter(Video.end_time >= a,Video.end_time <= b)
        qry1=set(qry1)
        qry2=set(qry2)
        qry3=set(qry3)
        qry1.union(qry2)
        qry1.union(qry3)
        print(type(qry1))
        return render_template('search.html',qry=qry1,form=form)
    return render_template('search.html',form=form)


if __name__ =='__main__':
    app.run(debug=True)
