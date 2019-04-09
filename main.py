import argparse
import csv
import datetime
import sys

import src.plot as sp
import src.weight as sw
import src.tweet as st

# Get command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("weight", help="Please set argument of your today's weight", type=float)
args = parser.parse_args()
t_weight = args.weight

# Get date
today = str(datetime.date.today().strftime("%m-%d"))

# Get date of first day and yesterday from CSV 
with open('weight.csv') as file:
    csv_file = csv.reader(file)
    csv_arr = [row for row in csv_file]
    if csv_arr[-1][0] == today:
        print("Error: Today's data is already exist.")
        sys.exit(1)
    y_weight = csv_arr[-1][1]
    f_weight = csv_arr[1][1]

# Update CSV
with open('weight.csv', 'a+') as file:
    csv.writer(file).writerow([today, t_weight])

# Generate graph from CSV
sp.Graph().plot_graph()

# Get difference of yesterday and first day, and format
msg = sw.Weight(t_weight, y_weight, f_weight, today).format_weight()

# Post to Twitter
img = "weight.png"
st.Tweet().tweet(msg, img)
print("Succeeded to post!")