from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateTimeField
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Optional, Length,NumberRange
import datetime

class enterdata(FlaskForm):
    camera_id = IntegerField('Camera Id:', default=None)
    start_time= DateTimeField('Start Time',render_kw={"placeholder": "YYYY-MM-DD HH:MM:SS"},default=datetime.datetime.utcnow,validators=[DataRequired()])
    end_time = DateTimeField('End Time', render_kw={"placeholder": "YYYY-MM-DD HH:MM:SS"},default=datetime.datetime.utcnow,validators=[DataRequired()])
    filepath=StringField('File Path',validators=[DataRequired()])
    submit = SubmitField('Upload')

class getinfoform(FlaskForm):
    camera_id = IntegerField('Camera Id:', default=None)
    start_time= DateTimeField('Start Time',render_kw={"placeholder": "YYYY-MM-DD HH:MM:SS"},default=datetime.datetime.utcnow)
    end_time = DateTimeField('End Time', render_kw={"placeholder": "YYYY-MM-DD HH:MM:SS"},default=datetime.datetime.utcnow)
    submit = SubmitField('Search')
