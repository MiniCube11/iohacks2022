from flask import Blueprint, render_template
from app.models import Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html')


@bp.route('/events')
def events():
    _events = Event.query.all()
    return render_template('main/events.html', events=_events)
