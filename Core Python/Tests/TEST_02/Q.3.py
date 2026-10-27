# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

radius = 20
length = 50
breadth = 40
cost = 35

circle = 3.14 * radius
rectangle = 2 * (length + breadth)

perimeter = circle + rectangle
total_wire = perimeter * 5
total_cost = total_wire * cost

print("Total fencing cost =", total_cost)
