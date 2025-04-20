#MapPlot.py
#Name:
#Date:
#Assignment:
# Step 1 - Import necessary packages
# Import necessary libraries
import cars  # CORGIS dataset module
import matplotlib.pyplot as plt

# Load the dataset
car_data = cars.get_car()

# Pick the first car with valid MPG data
for car in car_data:
    try:
        city = car['Fuel Information']['City mpg']
        highway = car['Fuel Information']['Highway mpg']
        make = car['Identification']['Make']
        model = car['Identification']['Model Year']

        # Validate MPG values
        if (
            isinstance(city, (int, float)) and isinstance(highway, (int, float)) and
            5 <= city <= 150 and 5 <= highway <= 150
        ):
            selected_car = f"{make} {model}"
            break  # Stop after finding the first valid car
    except (KeyError, TypeError):
        continue

# Plot the single car's MPG
plt.figure(figsize=(6, 6))
plt.scatter(city, highway, color='red', s=100)

# Add labels and title
plt.xlabel('City MPG')
plt.ylabel('Highway MPG')
plt.title(f'MPG for {selected_car}')
plt.xlim(0, 60)
plt.ylim(0, 60)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.savefig("Lab")


# The data tells the difference in highway and city mpg. The visual assist made it easy to see the difference.
