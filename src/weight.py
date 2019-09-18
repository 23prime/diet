import argparse
import csv
import datetime

def add_sign(f):
    if f < 0:
        return str(f)
    else:
        return "+" + str(f)

class Weight:
    def __init__(self, csv_name):
        self.csv_name = csv_name
        self.today = str(datetime.date.today().strftime("%m-%d"))
        self.t_weight = float()
        self.y_weight = float()
        self.f_weight = float()
        self.diff_y = float()
        self.diff_f = float()

    def today_weight(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "weight", help="Please set argument of your today's weight.",
            type=float)
        args = parser.parse_args()
        self.t_weight = float(args.weight)

    def weights(self):
        with open(self.csv_name) as file:
            csv_file = csv.reader(file)
            csv_arr = [row for row in csv_file]

            if csv_arr[-1][0] == self.today:
                print("Error: Today's data is already exist.")
                exit(1)

            self.y_weight = float(csv_arr[-1][1])
            self.f_weight = float(csv_arr[1][1])

    def diffs(self):
        self.diff_y = round(self.t_weight - self.y_weight, 1)
        self.diff_f = round(self.t_weight - self.f_weight, 1)

    def format_weight(self):
        self.today_weight()
        self.weights()
        self.diffs()

        self.diff_y = add_sign(self.diff_y)
        self.diff_f = add_sign(self.diff_f)

        return ("{}\n{} kg\n前日比： {} kg\n初日比： {} kg\n\n#ok_diet"
            .format(self.today, self.t_weight, self.diff_y, self.diff_f))

    def update_csv(self):
        with open(self.csv_name, 'a+') as file:
            csv.writer(file).writerow([self.today, self.t_weight])


