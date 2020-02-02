from flask_wtf import FlaskForm
#from wtforms_components import DateTimeField
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Optional, Length,NumberRange

class getinfoform(FlaskForm):
    cameraid=IntegerField('Camera Id:',default=None)
    startyear=IntegerField('Start Year:',validators=[NumberRange(min=1901,max=2155)])
    startmonth=IntegerField('Month:',validators=[NumberRange(min=1,max=12)])
    startday=IntegerField('Date:',validators=[NumberRange(min=1,max=31)])
    starthour=IntegerField('Hour',validators=[NumberRange(min=6,max=23)])
    startmin=IntegerField('Minute',validators=[NumberRange(min=0,max=59)])
    startsec=IntegerField('Second',validators=[NumberRange(min=0,max=59)])
    endyear=IntegerField('End Year',validators=[NumberRange(min=1901,max=2155)])
    endmonth=IntegerField('Month',validators=[NumberRange(min=1,max=12)])
    endday=IntegerField('Date',validators=[NumberRange(min=1,max=31)])
    endhour=IntegerField('Hour',validators=[NumberRange(min=6,max=23)])
    endmin=IntegerField('Minute',validators=[NumberRange(min=0,max=59)])
    endsec=IntegerField('Second',validators=[NumberRange(min=0,max=59)])
    submit=SubmitField('Search')
