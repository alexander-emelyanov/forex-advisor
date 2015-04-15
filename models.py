from app import db, bcrypt


class Market(db.Model):

    __tablename__ = 'market'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


class Symbol(db.Model):

    __tablename__ = 'symbol'

    id = db.Column(db.Integer, primary_key=True)
    market_id = db.Column(db.Integer, db.ForeignKey(Market.__tablename__ + ".id"), nullable=False)
    market = db.relationship('Market')
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


class Direction(db.Model):

    __tablename__ = 'direction'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


class Duration(db.Model):

    __tablename__ = 'duration'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


class Predictor(db.Model):

    __tablename__ = 'predictor'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


class Signal(db.Model):

    __tablename__ = 'signal'

    id = db.Column(db.Integer, primary_key=True)
    time_of_creation = db.Column(db.DateTime, nullable=False)
    opening_time = db.Column(db.DateTime, nullable=False)
    closing_time = db.Column(db.DateTime, nullable=False)
    symbol_id = db.Column(db.Integer, db.ForeignKey(Symbol.__tablename__ + ".id"), nullable=False)
    symbol = db.relationship('Symbol')
    direction_id = db.Column(db.Integer, db.ForeignKey(Direction.__tablename__ + ".id"), nullable=False)
    direction = db.relationship('Direction')
    duration_id = db.Column(db.Integer, db.ForeignKey(Duration.__tablename__ + ".id"), nullable=False)
    duration = db.relationship('Duration')
    predictor_id = db.Column(db.Integer, db.ForeignKey(Predictor.__tablename__ + ".id"), nullable=False)
    predictor = db.relationship('Predictor')


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    passhash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.passhash = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<id {}>'.format(self.id)