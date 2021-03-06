from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_login import current_user
from app import app, db, mail, login
from app.forms.events import AddEventForm
from app.models import Event
from flask_mailing import Message

bp = Blueprint('events', __name__)


@bp.route('/add', methods=['GET', 'POST'])
async def add_event():
    if not current_user.is_authenticated:
        return login.unauthorized()
    form = AddEventForm(request.form)
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

        def format_date(date):
            months = ['', "Jan", "Feb", "Mar", "Apr", "May",
                      "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            return f"{months[date.month]} {date.day}, {date.year}"

        message = Message(
            subject=f"FEMevents - {form.title.data} on {format_date(form.date.data)}",
            recipients=[app.config["MAIL_USERNAME"]],
            html=f"""<p>Hi there!</p>

<p>A new event {form.title.data} has been posted on FEMevents!</p>
<p>Check it out on <a href="http://127.0.0.1:5000/events">FEMevents</a>!</p>

<p><i>FEMevents Team</i></p>"""
        )
        await mail.send_message(message)

        flash("Event created")
        return redirect(url_for('main.index'))
    return render_template('events/add_event.html', form=form)


@bp.route('/<_id>/view')
def event_detail(_id):
    event = Event.query.get_or_404(_id)

    def format_date(date):
        months = ['', "Jan", "Feb", "Mar", "Apr", "May",
                  "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f"{months[date.month]} {date.day}, {date.year}"

    return render_template('events/event_detail.html', event=event, format_date=format_date)
