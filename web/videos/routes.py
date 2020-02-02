from flask import Blueprint,render_template,request
from web.videos.forms import getinfoform
from web.models import Video


video=Blueprint('video',__name__)

@video.route('/go',methods=['GET','POST'])
def go():
    form=getinfoform()
    if form.is_submitted():
        sm=form.startmonth.data
        if sm<10:
            sm='0'+str(sm)
        em=form.endmonth.data
        if em<10:
            em='0'+str(em)
        sd=form.startday.data
        if sd<10:
            sd='0'+str(sd)
        ed=form.endday.data
        if ed<10:
            ed='0'+str(ed)
        sh=form.starthour.data
        if sh<10:
            sh='0'+str(sh)
        eh=form.endhour.data
        if eh<10:
            eh='0'+str(eh)
        smm=form.startmin.data
        if smm<10:
            smm='0'+str(smm)
        emm=form.endday.data
        if emm<10:
            emm='0'+str(emm)
        ss=form.starthour.data
        if ss<10:
            ss='0'+str(ss)
        es=form.endhour.data
        if es<10:
            es='0'+str(es)
        a=str(form.startyear.data)+str(sm)+str(sd)+str(sh)+str(smm)+str(ss)
        b=str(form.endyear.data)+str(em)+str(ed)+str(eh)+str(emm)+str(es)
        c=form.cameraid.data
        a=int(a)
        b=int(b)
        if c is None:
            qry1=Video.query.filter(Video.start_time >= a,Video.end_time <= b).order_by(Video.camera_id,Video.start_time)
            qry2=Video.query.filter(Video.start_time >= a,Video.start_time <= b).order_by(Video.start_time)
            qry3=Video.query.filter(Video.end_time >= a,Video.end_time <= b).order_by(Video.camera_id,Video.start_time)
        else:
            qry1=Video.query.filter(Video.camera_id==c,Video.start_time <= a,Video.end_time >= b).order_by(Video.camera_id,Video.start_time)
            qry2=Video.query.filter(Video.camera_id==c,Video.start_time >= a,Video.start_time <= b).order_by(Video.start_time)
            qry3=Video.query.filter(Video.camera_id==c,Video.end_time >= a,Video.end_time <= b).order_by(Video.start_time)
        qry1=set(qry1)
        qry2=set(qry2)
        qry3=set(qry3)
        qry4=qry1.union(qry2)
        qry5=qry4.union(qry3)
        return render_template('search.html',qry=qry2,form=form)
    return render_template('search.html',form=form)
