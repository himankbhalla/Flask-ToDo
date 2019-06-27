from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_database.db'

# Initialize the database
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return 'Task: {}'.format(self.id)
# Index route

@app.route('/', methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        return 'hello'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
