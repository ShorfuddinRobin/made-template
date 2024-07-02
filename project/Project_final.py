import pandas as pd
import opendatasets as od
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

class Pipeline:

    def __init__(self):
        self.engine = create_engine('sqlite:///ProjectDatabase.db')

    def fetch_weather_data(self):
        dataset = 'https://www.kaggle.com/datasets/yakinrubaiat/bangladesh-weather-dataset'
        od.download(dataset)
        weather_data = pd.read_csv('bangladesh-weather-dataset/Temp_and_rain.csv')
        weather_data.to_sql('weather_data', con=self.engine, index=False, if_exists='replace')

    def fetch_rainfall_data(self):
        dataset = "https://www.kaggle.com/datasets/redikod/historical-rainfall-data-in-bangladesh"
        od.download(dataset)
        rainfall_data = pd.read_csv("historical-rainfall-data-in-bangladesh/customized_daily_rainfall_data.csv")
        rainfall_data.to_sql("rainfall_data", con=self.engine, index=False, if_exists='replace')

    def merge_datasets(self):
        # Load data from the database
        weather_data = pd.read_sql('weather_data', con=self.engine)
        rainfall_data = pd.read_sql('rainfall_data', con=self.engine)

        # Ensure date columns are in datetime format
        # Note: This step is unnecessary now as we're merging on Year and Month
        # weather_data['date'] = pd.to_datetime(weather_data['date'])
        # rainfall_data['date'] = pd.to_datetime(rainfall_data['date'])

        # Merge datasets on Year and Month columns
        merged_data = pd.merge(weather_data, rainfall_data, on=['Year', 'Month'], how='inner')

        # Handle missing values if necessary
        merged_data.dropna(inplace=True)

        # Save merged data to the database for future use
        merged_data.to_sql('merged_data', con=self.engine, index=False, if_exists='replace')

        return merged_data

    def analyze_relationship(self, merged_data):
        # Plot temperature vs. rainfall
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='tem', y='Rainfall', data=merged_data)
        plt.title('Temperature vs. Rainfall')
        plt.xlabel('Temperature')
        plt.ylabel('Rainfall')
        plt.show()

        # Calculate correlation
        correlation = merged_data['tem'].corr(merged_data['Rainfall'])
        print(f'Correlation between temperature and rainfall: {correlation}')

        # Perform linear regression analysis
        from sklearn.linear_model import LinearRegression
        X = merged_data[['tem']]
        y = merged_data['Rainfall']
        model = LinearRegression()
        model.fit(X, y)
        print(f'Linear Regression Coefficients: {model.coef_}')
        print(f'Linear Regression Intercept: {model.intercept_}')

    def initialize_pipeline(self):
        self.fetch_weather_data()
        self.fetch_rainfall_data()
        merged_data = self.merge_datasets()
        self.analyze_relationship(merged_data)

# Create an instance of the Pipeline class
pipeline_instance = Pipeline()

# Run the pipeline
pipeline_instance.initialize_pipeline()
