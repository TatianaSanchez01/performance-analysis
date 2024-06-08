import numpy as np
import time
import cProfiler

def matrix_multiplication(matrix1, matrix2):
  """Multiplies two matrices."""
  result = np.zeros_like(matrix1)
  for i in range(matrix1.shape[0]):
    for j in range(matrix2.shape[1]):
      for k in range(matrix2.shape[0]):
        result[i, j] += matrix1[i, k] * matrix2[k, j]
  return result

def main():
  """Generates and multiplies random matrices."""
  matrix_size = 1000  # Adjust this value for different test durations
  matrix1 = np.random.rand(matrix_size, matrix_size)
  matrix2 = np.random.rand(matrix_size, matrix_size)

  start_time = time.time()
  result = matrix_multiplication(matrix1, matrix2)
  end_time = time.time()
  elapsed_time = end_time - start_time

  print(f"Matrix multiplication took {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
  main()
    cProfile.run('main()')

