from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://svcreadonly:svcreadonly@localhost/flask_school'

db = SQLAlchemy(app)

class Students(db.Model):
    # __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(50))

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'subjects': student.subject}
        for student in students
    ]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run(debug=True)
