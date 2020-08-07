from flask import render_template, request, Blueprint
from testapp.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/events")
def events():
    return render_template('events.html', title='Events')

@main.route("/offers")
def offers():
    return render_template('offers.html', title='Offers')

@main.route("/calender")
def calender():
    return render_template('calender.html', title='Calender')

@main.route("/wishlist")
def wishlist():
    return render_template('wishlist.html', title='Your Cart')
