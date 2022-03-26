from flask import Blueprint, render_template, flash, url_for, redirect, request
from app import db
from app.forms.events import AddEventForm
from app.models import Event
from datetime import datetime

bp = Blueprint('events', __name__)


@bp.route('/add', methods=['GET', 'POST'])
def add_event():
    form = AddEventForm(request.form)
    print(form.errors, request.method == "POST", form.validate_on_submit())
    if request.method == "POST" and form.validate_on_submit():
        event = Event(
            title=form.title.data,
            date=form.date.data,
            description=form.description.data,
            is_virtual=form.is_virtual.data,
            location=form.location.data,
            website_link=form.website_link.data,
            register_link=form.register_link.data,
            organizer=form.organizer.data,
            event_type=form.event_type.data
        )
        db.session.add(event)
        db.session.commit()
        flash("Event created")
        return redirect(url_for('main.events'))
    return render_template('events/add_event.html', form=form)
