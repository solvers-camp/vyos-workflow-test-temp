import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    # Example of a potential SQL injection vulnerability
    user_id = flask.request.args.get('user_id')
    query = "SELECT * FROM users WHERE id = " + user_id
    result = db.engine.execute(query)
    return str(result.fetchall())
