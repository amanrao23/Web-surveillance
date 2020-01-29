from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class getinfoform(FlaskForm):
    startime=IntegerField()
    endtime=IntegerField()
    submit=SubmitField('Search')
