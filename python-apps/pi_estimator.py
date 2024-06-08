import random
import cProfile

def calculate_pi(iterations):
  """Estimates pi using the Monte Carlo method."""
  count_in_circle = 0
  for _ in range(iterations):
    x = random.random()
    y = random.random()
    if (x**2 + y**2) <= 1:
      count_in_circle += 1
  pi_estimate = 4 * count_in_circle / iterations
  return pi_estimate

def main():
  """Runs the pi calculation and prints the estimated value."""
  iterations = 1000000  # Adjust this value for different test durations
  pi = calculate_pi(iterations)
  print(f"Estimated value of pi: {pi}")

if __name__ == "__main__":
  main()
  cProfile.run('main()')
