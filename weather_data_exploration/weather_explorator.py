# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import os



class WeatherExplorator():

    def __init__(self,csv_path='seoul_one_year.csv'):
        # Load data
        self.data = pd.read_csv(csv_path)
        self.preprocess_data = self.preprocess()
        self.pred = None
        self.order = ""
        self.model = None

    def preprocess(self):
        long_data_df = self.data.iloc[2:][["latitude", "longitude"]].rename(columns={"latitude": "time", "longitude": "temp"})
        long_data_df["time"] = pd.to_datetime(long_data_df["time"])
        long_data_df["temp"] = long_data_df["temp"].apply(lambda x: float(x))
        return long_data_df

    def find_fit(self):
        # Finding the correct parameters of ARIMA model to preidct the temperature
        stepwise_fit = auto_arima(self.preprocess_data['temp'], trace=True, suppress_warnings=True)
        self.order = stepwise_fit.order
        return stepwise_fit
    
    def train_test_split(self):
        # Find the shape of the data
        print(self.preprocess_data.shape)
        train = self.preprocess_data.iloc[:-30]
        test = self.preprocess_data.iloc[-30:]
        print(train.shape, test.shape)
        return train, test

    def train_model(self):
        self.train, self.test = self.train_test_split()
        self.find_fit()
        # Using ARIMA model to predict the temperature
        model = ARIMA(self.train['temp'], order=self.order)
        self.model = model.fit()
        print(self.model.summary())
        return self.model
        
    def predict(self):
        # Prediction
        start = len(self.train)
        end = len(self.train) + len(self.test) - 1
        self.pred = self.model.predict(start=start, end=end, typ='levels').rename('ARIMA Predictions')
        return self.pred

    def plot(self):
        # Plotting them together
        plt.figure(figsize=(30, 10))
        plt.plot(self.preprocess_data["time"].iloc[-150:], self.preprocess_data["temp"].iloc[-150:], color = "blue", label = "temp", alpha=0.5)
        plt.plot(self.preprocess_data["time"].iloc[-30:], self.pred, color = "red", label = "predict_temp", ls="--", alpha=0.5)
        plt.xlabel("Date")
        plt.ylabel("Temperature (C)")
        plt.title("Seoul Temperature from Jan 1 to Feb 14 2023")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Main flow for the program
    we = WeatherExplorator()
    model = we.train_model()
    we.predict()
    we.plot()
