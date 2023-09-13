import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import timedelta, datetime

def read_log_file(log_file):
    # Read log file into a pandas DataFrame
    df = pd.read_csv(log_file, parse_dates=['Timestamp'])

    # Extract relevant columns
    df = df[['Timestamp', 'cpu-usage']]

    return df

def train_linear_regression(df):
    X = df['Timestamp'].map(datetime.toordinal).values.reshape(-1, 1)
    y = df['cpu-usage'].values.reshape(-1, 1)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model
def predict_cpu_usage(model, date):
    ordinal_date = datetime.strptime(date, '%Y-%m-%d').toordinal()
    predicted_cpu = model.predict([[ordinal_date]])

    return predicted_cpu[0][0]

def main():
    log_file = '2023-09-07-pub.log'  # Specify the name of the log file
    date_to_predict = '2023-09-08'  # Specify the date to predict CPU usage for

    # Read log file
    df = read_log_file(log_file)

    # Train linear regression model
    model = train_linear_regression(df)

    # Predict CPU usage for another day
    predicted_cpu = predict_cpu_usage(model, date_to_predict)
    print(f"Predicted CPU usage for {date_to_predict}: {predicted_cpu}")
    if __name__ == '__main__':
        main()