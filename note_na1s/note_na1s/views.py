
from flask import render_template, flash, redirect, url_for

from note_na1s import app, db
from note_na1s.models import Message
from note_na1s.forms import HelloForm

@app.route('/', methods=['GET','POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form ,messages=messages)
