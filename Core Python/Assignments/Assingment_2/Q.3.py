# Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Convert to meters and centimeters
total_inches = (feet * 12) + inches
meters = total_inches * 0.0254
centimeters = meters * 100

print(f"Total distance: {meters:.2f} meters or {centimeters:.2f} centimeters")