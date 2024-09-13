import numpy as np

# Parameters
total_sum = 10000  # Desired total sum
n = 10000  # Number of samples

# Start with a Poisson lambda (mean) value
lambda_value = 5

# Generate Poisson-distributed random numbers
poisson_data = np.random.poisson(lambda_value, n)

# Calculate the current sum of the generated values
current_sum = np.sum(poisson_data)

# Calculate the scaling factor
scaling_factor = total_sum / current_sum

# Scale the data to match the desired total sum
scaled_data = poisson_data * scaling_factor

# Round to ensure integers, as Poisson distribution values are integers
scaled_data = np.round(scaled_data).astype(int)

# Verify the result
new_sum = np.sum(scaled_data)
print(f"Sum of scaled data: {new_sum}")

# Optionally, print the first few values
print(scaled_data[:10])
