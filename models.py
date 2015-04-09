from app import db


class Symbol(db.Model):

    __tablename__ = 'symbol'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)