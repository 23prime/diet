def add_sign(f):
    if f < 0:
        return str(f)
    else:
        return "+" + str(f)

class Weight:
    def __init__(self, t, y, f, today):
        self.today = today
        self.t_weight = float(t)
        y_weight = float(y)
        f_weight = float(f)
        self.diff_y = round(self.t_weight - y_weight, 1)
        self.diff_f = round(self.t_weight - f_weight, 1)

    def format_weight(self):
        self.t_weight = str(self.t_weight)
        self.diff_y = add_sign(self.diff_y)
        self.diff_f = add_sign(self.diff_f)

        return "{}\n{} kg\n前日比： {} kg\n初日比： {} kg\n\n#ok_diet".format(self.today, self.t_weight, self.diff_y, self.diff_f)
