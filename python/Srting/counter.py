def create_counter(init):
  """
  Creates a counter object with increment, decrement and reset methods.

  Args:
      init: The initial value of the counter.

  Returns:
      A counter object with the following methods:
          increment: Increments the counter by 1 and returns the new value.
          decrement: Decrements the counter by 1 and returns the new value.
          reset: Resets the counter to the specified value (defaults to the initial value) and returns the new value.
  """

  def increment():
    nonlocal init
    init += 1
    return init

  def decrement():
    nonlocal init
    init -= 1
    return init

  def reset(new_init=None):
    nonlocal init
    init = new_init or init
    return init

  return {
      "increment": increment,
      "decrement": decrement,
      "reset": reset,
  }

# Example usage
counter = create_counter(5)
calls = ["increment", "reset", "decrement"]

output = [counter[call]() for call in calls]
print(output)  # Output: [6, 5, 4]
