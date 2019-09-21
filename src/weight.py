import argparse
import datetime
from src.weights import Weights, db

def add_sign(f):
    if f < 0:
        return str(f)
    else:
        return "+" + str(f)

class Weight:
    def __init__(self, csv_name):
        self.today = str(datetime.date.today().strftime("%m-%d"))
        self.t_weight = float()
        self.first = Weights.query.first()
        self.last = Weights.query.all()[-1]
        self.f_weight = float(self.first.weight)
        self.y_weight = float(self.last.weight)

    def today_weight(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "weight", help="Please set argument of your today's weight.",
            type=float)
        args = parser.parse_args()
        self.t_weight = float(args.weight)
        
    def format_weight(self):
        self.today_weight()

        if self.last.date == self.today:
            print("Error: Today's data is already exist.")
            exit(1)

        diff_f = round(self.t_weight - self.f_weight, 1)
        diff_y = round(self.t_weight - self.y_weight, 1)
        diff_y = add_sign(diff_y)
        diff_f = add_sign(diff_f)

        return ("{}\n{} kg\n前日比： {} kg\n初日比： {} kg\n\n#ok_diet"
            .format(self.today, self.t_weight, diff_y, diff_f))

    def update_db(self):
        db.session.add(Weights(date = self.today, weight = self.t_weight))
        db.session.commit()
