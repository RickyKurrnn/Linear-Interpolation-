import numpy as np

def linear_interpolation(x_values, y_values, x_query):
    """Perform linear interpolation to estimate y for given x_query."""
    return np.interp(x_query, x_values, y_values)

def extrapolation(x_values, y_values, x_query):
    """Perform extrapolation using linear regression for x_query values beyond the range."""
    coeffs = np.polyfit(x_values, y_values, 1)  # Linear regression (degree 1)
    poly = np.poly1d(coeffs)
    return poly(x_query)

def calculate_errors(predicted, actual):
    """Calculate absolute and relative errors."""
    abs_error = abs(predicted - actual)
    rel_error = (abs_error / actual) * 100 if actual != 0 else float('inf')
    return abs_error, rel_error

def score_based_on_error(abs_error):
    """Score predictions based on absolute error (lower is better)."""
    return max(100 - abs_error, 0)

# Input data
years = [2010, 2015, 2016, 2017, 2018]
population = [238, 255, 258, 261, 264]

# User Inputs
print("Available years:", years)
query_year = float(input("Enter the year you want to predict population for: "))
actual_population = float(input("Enter the actual population (if known): "))

# Determine whether to interpolate or extrapolate
if min(years) <= query_year <= max(years):
    predicted_population = linear_interpolation(years, population, query_year)
    method = "Interpolation"
else:
    predicted_population = extrapolation(years, population, query_year)
    method = "Extrapolation"

# Calculate errors and score
abs_error, rel_error = calculate_errors(predicted_population, actual_population)
score = score_based_on_error(abs_error)

# Display Results
print("\nResults:")
print(f"Method: {method}")
print(f"Predicted Population for {query_year}: {predicted_population:.2f}")
print(f"Absolute Error: {abs_error:.2f}")
print(f"Relative Error: {rel_error:.2f}%")
print(f"Prediction Score: {score:.2f}")
