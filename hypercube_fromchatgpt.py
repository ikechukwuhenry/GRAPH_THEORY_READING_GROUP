class Hypercube:
    def __init__(self, dimensions, initial_value=None):
        self.dimensions = dimensions
        self.initial_value = initial_value
        self.data = self._create_hypercube(dimensions, initial_value)

    def _create_hypercube(self, dimensions, value):
        if len(dimensions) == 1:
            return [value] * dimensions[0]
        return [self._create_hypercube(dimensions[1:], value) for _ in range(dimensions[0])]

    def _get_subcube(self, coords):
        subcube = self.data
        for coord in coords:
            subcube = subcube[coord]
        return subcube

    def get(self, coords):
        subcube = self._get_subcube(coords[:-1])
        return subcube[coords[-1]]

    def set(self, coords, value):
        subcube = self._get_subcube(coords[:-1])
        subcube[coords[-1]] = value

    def __repr__(self):
        return repr(self.data)

# Example usage:
# Create a 3x3x3 hypercube with initial value 0
hypercube = Hypercube([3, 3, 3], initial_value=0)

# Set a value in the hypercube
hypercube.set([1, 1, 1], 42)

# Get a value from the hypercube
value = hypercube.get([1, 1, 1])
print(value)  # Output: 42

# Print the entire hypercube
print(hypercube)
