import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load historical cash flow data from a CSV file
def load_cash_flow_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    # Ensure the index is a valid time series index before setting frequency
    if not data.index.is_monotonic_increasing:
        data = data.sort_index()
    data.index.freq = pd.infer_freq(data.index)  # Infer frequency automatically
    # Preserve AccountNo and Branch columns
    data = data[['AccountNo', 'Branch', 'Opening Balance', 'Cash In', 'Cash Out', 'Closing Balance']]
    return data

# Visualize the historical cash flow data
def visualize_cash_flow(data):
    plt.figure(figsize=(10, 6))
    # Group by Branch for visualization
    for branch in data['Branch'].unique():
        branch_data = data[data['Branch'] == branch]
        plt.plot(branch_data.index, branch_data['Closing Balance'], label=f'Branch: {branch}')
    plt.title('Historical Cash Flow by Branch')
    plt.figure(figsize=(12, 6))
    for branch in data['Branch'].unique():
        branch_data = data[data['Branch'] == branch]
        plt.plot(branch_data.index, branch_data['Cash In'], label=f'Cash In - Branch: {branch}', linestyle='--')
        plt.plot(branch_data.index, branch_data['Cash Out'], label=f'Cash Out - Branch: {branch}', linestyle=':')
    plt.title('Cash Flow Trends by Branch')
    plt.xlabel('Date')
    plt.ylabel('Cash Flow')
    plt.legend()
    plt.show()
    plt.xlabel('Date')
    plt.ylabel('Closing Balance')
    plt.legend()
    plt.show()

# Split the data into training and testing sets
def split_data(data, test_size=0.2):
    # Split data while preserving AccountNo and Branch columns
    train_size = int(len(data) * (1 - test_size))
    train, test = data.iloc[:train_size], data.iloc[train_size:]
    return train, test

# Build and train an ARIMA model
def train_arima_model(train_data, order=(1, 1, 1)):
    # Ensure only the 'Closing Balance' column is used for training
    train_data_univariate = train_data['Closing Balance']
    model = ARIMA(train_data_univariate, order=order)
    model_fit = model.fit()
    return model_fit

# Make predictions on the test set
def make_predictions(model_fit, test_data):
    predictions = model_fit.forecast(steps=len(test_data))
    # Preserve AccountNo and Branch columns in predictions using .loc to avoid SettingWithCopyWarning
    test_data = test_data.copy()  # Ensure a deep copy to avoid warnings
    test_data['Predicted Closing Balance'] = predictions.values  # Add predictions as a new column
    test_data['Predicted Closing Balance'].fillna(0, inplace=True)  # Handle NaN values explicitly
    return test_data

def evaluate_model(test_data):
    # Drop rows with NaN in either column
    test_data_cleaned = test_data.dropna(subset=['Closing Balance', 'Predicted Closing Balance'])

    # Check if there's any data left
    if test_data_cleaned.empty:
        return None  # Return None if no valid data is available
    else:
        mse = mean_squared_error(
            test_data_cleaned['Closing Balance'],
            test_data_cleaned['Predicted Closing Balance']
        )
        return mse

# Example usage
if __name__ == "__main__":
    file_path = "cash_flow_data.csv"  # Replace with your CSV file path
    data = load_cash_flow_data(file_path)
    visualize_cash_flow(data)

    train, test = split_data(data)
    model_fit = train_arima_model(train)
    test_with_predictions = make_predictions(model_fit, test)
    
    mse = evaluate_model(test_with_predictions)
    print(f"Mean Squared Error: {mse}")

    file_path = "cash_flow_data.csv"  # Replace with your CSV file path
    data = load_cash_flow_data(file_path)
    visualize_cash_flow(data)
    
    train, test = split_data(data)
    model_fit = train_arima_model(train)
    test_with_predictions = make_predictions(model_fit, test)
    
    mse = evaluate_model(test_with_predictions)
    print(f"Mean Squared Error: {mse}")
    
    # Visualize the predictions alongside actual data
    def visualize_predictions(data, predictions):
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Closing Balance'], label='Actual Closing Balance', color='blue')
        plt.plot(data.index[-len(predictions):], predictions, label='Predicted Closing Balance', color='orange')
        plt.title('Actual vs Predicted Closing Balance')
        plt.xlabel('Date')
        plt.ylabel('Closing Balance')
        plt.legend()
        plt.show()
    
        visualize_predictions(test_with_predictions, test_with_predictions['Predicted Closing Balance'])
