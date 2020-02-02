from web import db

class Video(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    camera_id=db.Column(db.Integer)
    start_time=db.Column(db.Integer)
    end_time=db.Column(db.Integer)
    filepath=db.Column(db.String)
