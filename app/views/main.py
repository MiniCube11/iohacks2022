from flask import Blueprint, render_template
from app.models import Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/events')
def events():
    _events = Event.query.all()

    def format_date(date):
        months = ['', "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return f"{months[date.month]} {date.day}"

    return render_template('main/events.html', events=_events, format_date=format_date)
