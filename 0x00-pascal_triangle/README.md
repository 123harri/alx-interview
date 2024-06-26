# Pascal's Triangle Generator

This Python script generates Pascal's triangle up to a specified number of rows.

## Usage

### Requirements

- Python 3.x

### Function

#### `pascal_triangle(n)`

Generates Pascal's triangle up to `n` rows.

- **Arguments:**
  - `n` (int): Number of rows in Pascal's triangle. Must be a positive integer.

- **Returns:**
  - List of lists: Pascal's triangle represented as a list of lists of integers.

If `n` is less than or equal to 0, the function returns an empty list.

### Example

```python
from pascal_triangle import pascal_triangle

# Example usage
n = 5
triangle = pascal_triangle(n)

# Print the triangle
for row in triangle:
    print(row)
