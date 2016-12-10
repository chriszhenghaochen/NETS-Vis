import script.plot.place_occupants as po
import data
import matplotlib.pyplot as plt


# ---------------- Example 1 ----------------
# create a blank plot to draw on
fig1, ax1 = plt.subplots()

# plot a stacked area plot of how many people are in ride 32
po.plot_stacked_area([32], ax1)
# add a legend to the plot saying which ride we're looking at
po.add_legend([32], ax1)


# ---------------- Example 2 ----------------
# create a blank plot to draw on
fig2, ax2 = plt.subplots()

# plot a stacked area plot of how many people are in ride 32 and in ride 63
po.plot_stacked_area([32, 63], ax2)
# add a legend to the plot saying which ride we're looking at
po.add_legend([32, 63], ax2)


# ---------------- Example 3 ----------------
# create a blank plot to draw on
fig3, ax3 = plt.subplots()
# plot all the rides of one category
kp = data.read_key_points()
# true if a ride is a thrill ride
idx = kp['category'] == 'Thrill Rides'
# use the true/false vector to select rows of the key points
thrill_rides = kp[idx]
# or in one line
thrill_rides = kp[kp['category'] == 'Thrill Rides']

# get just the ids
place_ids = kp[kp['category'] == 'Thrill Rides'].place_id.values

# plot a stacked plot of the ids
po.plot_stacked_area(place_ids, ax3)
# add a legend to the plot saying which ride we're looking at
po.add_legend(place_ids, ax3)


# ---------------- Example 4 ----------------
# create a blank plot to draw on
fig4, ax4 = plt.subplots()

# here you can choose if you want the start points, the end points, and/or the lines
po.plot_scatter([32], ax4, types=['start', 'end', 'lines'])
po.add_legend(place_ids, ax4)


plt.show()


