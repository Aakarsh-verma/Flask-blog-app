from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from testapp import db, bcrypt


events = Blueprint('events', __name__)


@events.route("/events/concerts")
def concerts():
    return render_template('events/concerts.html', title='Concerts')

@events.route("/events/concert1")
def concert1():
    return render_template('concerts/concert1.html', title='Concert1')

@events.route("/events/concert2")
def concert2():
    return render_template('concerts/concert2.html', title='Concert1')

@events.route("/events/concert3")
def concert3():
    return render_template('concerts/concert3.html', title='Concert1')


@events.route("/events/fine_arts")
def fine_arts():
    return render_template('events/fine_arts.html', title='Fine Arts')

@events.route("/events/fine_arts1")
def fine_arts1():
    return render_template('fine_arts/fine_arts1.html', title='Fine Arts1')

@events.route("/events/fine_arts2")
def fine_arts2():
    return render_template('fine_arts/fine_arts2.html', title='Fine Arts2')

@events.route("/events/fine_arts3")
def fine_arts3():
    return render_template('fine_arts/fine_arts3.html', title='Fine Arts3')



@events.route("/events/gaming")
def gaming():
    return render_template('events/gaming.html', title='Gaming')

@events.route("/events/gaming1")
def gaming1():
    return render_template('gaming/gaming1.html', title='Gaming1')

@events.route("/events/gaming2")
def gaming2():
    return render_template('gaming/gaming2.html', title='Gaming2')

@events.route("/events/gaming3")
def gaming3():
    return render_template('gaming/gaming3.html', title='Gaming3')



@events.route("/events/informals")
def informals():
    return render_template('events/informals.html', title='Informals')

@events.route("/events/informals1")
def informals1():
    return render_template('informals/informals1.html', title='Informals1')

@events.route("/events/informals2")
def informals2():
    return render_template('informals/informals2.html', title='Informals-2')

@events.route("/events/informals3")
def informals3():
    return render_template('informals/informals3.html', title='Informals-3')



@events.route("/events/literary_arts")
def literary_arts():
    return render_template('events/literary_arts.html', title='Literary Arts')

@events.route("/events/literary_arts1")
def literary_arts1():
    return render_template('literary_arts/literary_arts1.html', title='Literary Arts-1')

@events.route("/events/literary_arts2")
def literary_arts2():
    return render_template('literary_arts/literary_arts2.html', title='Literary Arts-2')

@events.route("/events/literary_arts3")
def literary_arts3():
    return render_template('literary_arts/literary_arts3.html', title='Literary Arts-3')


@events.route("/events/management")
def management():
    return render_template('events/management.html', title='Management')

@events.route("/events/management1")
def management1():
    return render_template('management/management1.html', title='Management-1')

@events.route("/events/management2")
def management2():
    return render_template('management/management2.html', title='Management-2')

@events.route("/events/management3")
def management3():
    return render_template('management/management3.html', title='Management-3')



@events.route("/events/performing_arts")
def performing_arts():
    return render_template('events/performing_arts.html', title='Performing Arts')

@events.route("/events/performing_arts1")
def performing_arts1():
    return render_template('performing_arts/performing_arts1.html', title='Performing Arts-1')

@events.route("/events/performing_arts2")
def performing_arts2():
    return render_template('performing_arts/performing_arts2.html', title='Performing Arts-2')

@events.route("/events/performing_arts3")
def performing_arts3():
    return render_template('performing_arts/performing_arts3.html', title='Performing Arts-3')



@events.route("/events/sports")
def sports():
    return render_template('events/sports.html', title='Sports')

@events.route("/events/sports1")
def sports1():
    return render_template('sports/sports1.html', title='Sports-1')

@events.route("/events/sports2")
def sports2():
    return render_template('sports/sports2.html', title='Sports-2')

@events.route("/events/sports3")
def sports3():
    return render_template('sports/sports3.html', title='Sports-3')



@events.route("/events/tech_events")
def tech_events():
    return render_template('events/tech_events.html', title='Technical Events')

@events.route("/events/tech_events1")
def tech_events1():
    return render_template('tech_events/tech_events1.html', title='Technical Events-1')

@events.route("/events/tech_events2")
def tech_events2():
    return render_template('tech_events/tech_events2.html', title='Technical Events-2')

@events.route("/events/tech_events3")
def tech_events3():
    return render_template('tech_events/tech_events3.html', title='Technical Events-3')



@events.route("/events/tech_workshops")
def tech_workshops():
    return render_template('events/tech_workshops.html', title='Technical Workshops')

@events.route("/events/tech_workshops1")
def tech_workshops1():
    return render_template('tech_workshops/tech_workshops1.html', title='Technical Workshops-1')

@events.route("/events/tech_workshops2")
def tech_workshops2():
    return render_template('tech_workshops/tech_workshops2.html', title='Technical Workshops-2')

@events.route("/events/tech_workshops3")
def tech_workshops3():
    return render_template('tech_workshops/tech_workshops3.html', title='Technical Workshops-3')



@events.route("/events/workshops")
def workshops():
    return render_template('events/workshops.html', title='Workshops')

@events.route("/events/workshops1")
def workshops1():
    return render_template('workshops/workshops1.html', title='Workshops-1')

@events.route("/events/workshops2")
def workshops2():
    return render_template('workshops/workshops2.html', title='Workshops-2')

@events.route("/events/workshops3")
def workshops3():
    return render_template('workshops/workshops3.html', title='Workshops-3')
