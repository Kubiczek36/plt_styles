import matplotlib.pyplot as plt
from pltstyles import Styles

# Create an instance of the Styles class
styles = Styles(plt)

# Set the style to 'scandic'
styles.apply_style('scandic')

# Generate some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot the data
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Plot')

# Show the plot
plt.show()
