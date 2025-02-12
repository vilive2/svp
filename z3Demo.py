from z3 import *

# Define variables
x = Int('x')
y = Int('y')

# Create a solver instance
solver = Solver()

# Add constraints
solver.add(x + y == 10)
solver.add(x - y == 4)

# Check if a solution exists
if solver.check() == sat:
    model = solver.model()
    print(model)
else:
    print("No solution found")
