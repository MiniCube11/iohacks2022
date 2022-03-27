from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_login import login_required
from app import db
from app.forms.events import AddEventForm
from app.models import Event

bp = Blueprint('events', __name__)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
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


@bp.route('/<_id>/view')
def event_detail(_id):
    event = Event.query.get_or_404(_id)

    def format_date(date):
        months = ['', "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f"{months[date.month]} {date.day}, {date.year}"

    return render_template('events/event_detail.html', event=event, format_date=format_date)
