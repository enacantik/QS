app = Flask(__name__)

@app.route('/')
def index(:
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST'
        return login()

from flask import render_template

@app.route('hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello, html', name=name)

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<user_name')
def profile(user_name)
    return '{}\'s profile'.format(escape(user_name))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', user_name='John Doe'))