import numpy as np

from utils.accuracy import calculate_accuracy

def randmized_binary_search_guess(integer: int) -> int:
  """
  Guesses the given integer using randomized binary search. The idea is that
  on each iteration the integer is guessed randomly, but but in case of a miss,
  the number is guessed again, but the range of random numbers is reduced
  according to the guessed number at the previous step

  Args:
      integer (int): an integer to guess

  Returns:
      int: amount of attempts to guess the given integer
  """

  low = 1
  high = 101
  attempts = 0
  
  while True:
    attempts += 1
    guessed_integer = np.random.randint(low, high)

    if integer == guessed_integer:
      break # the integer has guessed, exit the loop
      
    if integer > guessed_integer:
      # the integer is larger than the guessed integer, so we can consider it
      # as a low border of random number range
      low = guessed_integer
      
    if integer < guessed_integer:
      # the integer is less than the guessed integer, so we can consider it
      # as a high border of random numbers range
      high = guessed_integer

  return attempts

# RUN
if __name__ == '__main__':
    calculate_accuracy(randmized_binary_search_guess)
