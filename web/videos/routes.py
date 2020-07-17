from flask import Blueprint, render_template, request, redirect, url_for
from web.videos.forms import getinfoform, enterdata
from web.models import Video
from web import db

video = Blueprint('video', __name__)


@video.route('/submit', methods=['GET', 'POST'])
def upload():
    form = enterdata()
    if form.is_submitted():
        s_time = form.start_time.data
        e_time = form.end_time.data
        new_task = Video(camera_id=form.camera_id.data, start_time=form.start_time.data, end_time=form.end_time.data, filepath=form.filepath.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('video.upload'))
    return render_template('post.html', form=form)


@video.route('/go', methods=['GET', 'POST'])
def go():
    form = getinfoform()
    if form.is_submitted():
        c = form.camera_id.data
        a = form.start_time.data
        b = form.end_time.data
        # a=int(a)
        # b=int(b)
        if c is None:
            qry1 = Video.query.filter(Video.start_time >= a, Video.end_time <= b).order_by(Video.camera_id,
                                                                                           Video.start_time)
            qry2 = Video.query.filter(Video.start_time >= a, Video.start_time <= b).order_by(Video.start_time)
            qry3 = Video.query.filter(Video.end_time >= a, Video.end_time <= b).order_by(Video.camera_id,
                                                                                         Video.start_time)
        else:
            qry1 = Video.query.filter(Video.camera_id == c, Video.start_time <= a, Video.end_time >= b).order_by(
                Video.camera_id, Video.start_time)
            qry2 = Video.query.filter(Video.camera_id == c, Video.start_time >= a, Video.start_time <= b).order_by(
                Video.start_time)
            qry3 = Video.query.filter(Video.camera_id == c, Video.end_time >= a, Video.end_time <= b).order_by(
                Video.start_time)
        qry1 = set(qry1)
        qry2 = set(qry2)
        qry3 = set(qry3)
        qry4 = qry1.union(qry2)
        qry5 = qry4.union(qry3)
        return render_template('search.html', qry=qry5, form=form)
    return render_template('search.html', form=form)
