# Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)


area = float(input("Enter area of one wall: "))
interior = float(input("Enter interior paint cost per unit: "))
exterior = float(input("Enter exterior paint cost per unit: "))

interior_cost = 8 * area * interior
exterior_cost = 6 * area * exterior

total = interior_cost + exterior_cost

print("Interior paint cost =", interior_cost)
print("Exterior paint cost =", exterior_cost)
print("Total paint cost =", total)
