import sys

import src.plot as sp
import src.weight as sw
import src.tweet as st

# Define file names
img_file = 'weight.png'

weight = sw.Weight()
weight_msg = weight.format_weight()

# Ask to do or not
line = "--------------------\n"
print(
    "{}{}\n{}Add today's data and post this message with \"{}\"? [Y/n]"
    .format(line, weight_msg, line, img_file))
ans = input().strip().lower()

if not ans in ['', 'y','yes']:
    print("Canceled.")
    exit(0)

# Run
weight.update_db()
sp.Graph().plot_graph()
st.Tweet().tweet(weight_msg, img_file)
print("Success!")
