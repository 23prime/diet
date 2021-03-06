import datetime

from diet.config import db
from diet.models.weights import Weights


def add_sign(f):
    if f < 0:
        return str(f)
    else:
        return "+" + str(f)


class Weight(object):
    def __init__(self, t_weight):
        self.today = str(datetime.date.today().strftime("%m-%d"))
        self.t_weight = float(t_weight)
        self.first = Weights.query.first()
        self.last = Weights.query.all()[-1]
        self.f_weight = float(self.first.weight)
        self.y_weight = float(self.last.weight)

    def format_weight(self):
        if self.last.date == self.today:
            raise WeightsAlreadyExistException

        diff_f = round(self.t_weight - self.f_weight, 1)
        diff_y = round(self.t_weight - self.y_weight, 1)
        diff_y = add_sign(diff_y)
        diff_f = add_sign(diff_f)

        return ("{}\n{} kg\n前日比： {} kg\n初日比： {} kg\n\n#ok_diet".format(
            self.today, self.t_weight, diff_y, diff_f))

    def update_db(self):
        try:
            db.session.add(Weights(date=self.today, weight=self.t_weight))
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise WeightsDBException
        finally:
            db.session.close()

    def delete_rec(self):
        try:
            rec = Weights.query().filter(Weights.date == self.today,
                                         Weights.weight == self.t_weight)
            db.session.delete(rec)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise WeightsDBException
        finally:
            db.session.close()


class WeightsDBException(Exception):
    pass


class WeightsAlreadyExistException(Exception):
    pass
