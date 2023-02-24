from . import db


class Medical_History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_client = db.Column(db.String, nullable=False)
    name_doctor = db.Column(db.String, nullable=False)
    diagnosis = db.Column(db.String, nullable=False)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Integer, nullable=False)
    inn = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String, nullable=False)
    date_of_application = db.Column(db.Integer)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Integer, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    experience = db.Column(db.String, nullable=False)

