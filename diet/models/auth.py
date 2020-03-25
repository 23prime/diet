from diet.config import db


class Auth(db.Model):
    __tablename__ = 'passes'
    __table_args__ = {'schema': 'diet'}
    password = db.Column(db.String(100), primary_key=True)

    def __repr__(self):
        return "Auth({}, {})".format(self.password)
