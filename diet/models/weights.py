from diet.config import db

class Weights(db.Model):
    __tablename__ = 'weights'
    __table_args__ = {'schema': 'diet'}
    date = db.Column(db.String(5), primary_key = True)
    weight = db.Column(db.String(4))

    def __repr__(self):
        return "Weights({}, {})".format(self.date, self.weight)
