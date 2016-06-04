import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1, 2), ylim=(-1, 2))
polygon = plt.Polygon([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
ax.add_patch(polygon)

# Function to be called when mouse is clicked
def on_click(event):
    if polygon.contains_point((event.x, event.y)):
        polygon.set_facecolor(np.random.random(3))
        fig.canvas.draw()

# Connect the click function to the button press event
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()