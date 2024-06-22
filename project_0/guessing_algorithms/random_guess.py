import numpy as np

from utils.accuracy import calculate_accuracy

def random_guess(integer:int=1) -> int:
  """
  Randomly guesses the given integer.

  Args:
      integer (int, optional): an integer to guess. Defaults to 1.

  Returns:
      int: amount of attempts to guess the given integer
  """
  
  attempts = 0
  
  while True:
      attempts += 1
      guessed_integer = np.random.randint(1, 101)
      
      if integer == guessed_integer:
          break # the integer has guessed, exit the loop

  return attempts

# RUN
if __name__ == '__main__':
    calculate_accuracy(random_guess)
