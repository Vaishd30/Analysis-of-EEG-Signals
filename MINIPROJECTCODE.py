import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load data from Excel file
df = pd.read_excel('hamsnehaA.xlsx')
df.fillna(df.mean(), inplace=True)

# Extract FFT values and frequency
fft = df[['Frequency', 'Value']].values

# Plot the FFT values vs frequency
plt.scatter(fft[:, 1], fft[:, 0])
plt.xlabel('Frequency')
plt.ylabel('FFT Value')
plt.title('EEG Signal FFT')
plt.show()

# Fit linear regression model to data
reg = LinearRegression().fit(fft[:, 1].reshape(-1, 1), fft[:, 0].reshape(-1, 1))

# Compute predictions using regression model
pred = reg.predict(fft[:, 1].reshape(-1, 1))
residuals = fft[:, 0] - pred[:, 0]

# Print regression coefficients
print('Intercept:', reg.intercept_)
print('Coefficients:', reg.coef_)

# Evaluate model performance
mse = mean_squared_error(fft[:, 0], pred)
r2 = r2_score(fft[:, 0], pred)
print('Mean squared error:', mse)
print('R-squared:', r2)

# Calculate concentration level using new formula
fft_max = np.max(fft[:, 1])
fft_min = np.min(fft[:, 1])
fft_mean = np.mean(fft[:, 1])
concentration = (fft_max - fft_min) / fft_mean

# Print concentration level
print('Concentration level:', concentration)

# Plot regression line
plt.scatter(fft[:, 1], fft[:, 0])
plt.plot(fft[:, 1], pred, color='red')
plt.xlabel('FFT Values')
plt.ylabel('Frequency')
plt.title('Regression Line')
plt.show()

# Plot residual plot
plt.scatter(fft[:, 1], residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Residual Plot')
plt.xlabel('FFT Values')
plt.ylabel('Residuals')
plt.show()