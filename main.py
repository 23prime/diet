import sys

import src.plot as sp
import src.weight as sw
import src.tweet as st

# Define file names
file_name = 'weight'
csv_name = file_name + '.csv'
img_name = file_name + '.png'

weight = sw.Weight(csv_name)
weight_msg = weight.format_weight()

# Ask to do or not
line = "--------------------\n"
print(
    "{}{}\n{}Add today's data and post this message with \"{}\"? [Y/n]"
    .format(line, weight_msg, line, img_name))
ans = input().strip().lower()

if not ans in ['', 'y','yes']:
    print("Canceled.")
    exit(0)

# Run
weight.update_csv()
sp.Graph().plot_graph()
st.Tweet().tweet(weight_msg, img_name)
print("Success!")
