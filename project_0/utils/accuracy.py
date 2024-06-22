import numpy as np
from typing import Callable

def calculate_accuracy(guess_number_function:Callable[[int], int]) -> int:
  """
  Checks how many attempts in average the given function takes to guess a random
  integer on 1000 repeats

  Args:
      guess_number_function (Callable[[int], int]): a function that guesses a random integer

  Returns:
      int: average amount of attempts to guess a random integer
  """

  np.random.seed(1) # to have an ability to get same random numbers for each call
  
  test_integers = np.random.randint(1, 101, size=(1000)) # test numbers
  attempts = []

  for integer in test_integers:
    attempts.append(guess_number_function(integer))

  score = int(np.mean(attempts)) # average amount of attempts

  print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
  
  return score
