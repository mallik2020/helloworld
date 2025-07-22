def greet(name):
  """Greets the person passed in as a parameter."""
  return f"Hello, {name}!"

def add(x, y):
  """Add two numbers and return the result."""
  return x + y

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

if __name__ == "__main__":
  print(greet("World"))
  print(add(5, 3))
  print(is_even(4))
  print(is_even(7))