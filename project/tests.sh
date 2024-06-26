#!/bin/bash

# Create a function to check the existence of a file
check_file_exists() {
    if [ ! -f "$1" ]; then
        echo "Test failed: $1 does not exist."
        exit 1
    else
        echo "Test passed: $1 exists."
    fi
}

# Run the data pipeline
python -c "
import pandas as pd
import opendatasets as od
from sqlalchemy import create_engine

class Pipeline:

    def __init__(self):
        self.engine = create_engine('sqlite:///ProjectDatabase.db')

    def fetch_weather_data(self):
        dataset = 'https://www.kaggle.com/datasets/yakinrubaiat/bangladesh-weather-dataset'
        od.download(dataset, force=True)  # Force re-download
        weather_data = pd.read_csv('bangladesh-weather-dataset/Temp_and_rain.csv')
        weather_data.to_sql('weather_data', con=self.engine, index=False, if_exists='replace')

    def fetch_rainfall_data(self):
        dataset = 'https://www.kaggle.com/datasets/redikod/historical-rainfall-data-in-bangladesh'
        od.download(dataset, force=True)  # Force re-download
        rainfall_data = pd.read_csv('historical-rainfall-data-in-bangladesh/customized_daily_rainfall_data.csv')
        rainfall_data.to_sql('rainfall_data', con=self.engine, index=False, if_exists='replace')

    def merge_datasets(self):
        # Load data from the database
        weather_data = pd.read_sql('weather_data', con=self.engine)
        rainfall_data = pd.read_sql('rainfall_data', con=self.engine)

        # Check if 'Day' column exists before dropping it
        if 'Day' in weather_data.columns:
            weather_data.drop(columns=['Day'], inplace=True)
        if 'Day' in rainfall_data.columns:
            rainfall_data.drop(columns=['Day'], inplace=True)

        # Merge datasets on Year and Month columns
        merged_data = pd.merge(weather_data, rainfall_data, on=['Year', 'Month'], how='inner')

        # Handle missing values if necessary
        merged_data.dropna(inplace=True)

        # Show the merged dataset
        print(merged_data)  # Show entire merged dataset

        return merged_data

    def initialize_pipeline(self):
        self.fetch_weather_data()
        self.fetch_rainfall_data()
        merged_data = self.merge_datasets()
        merged_data.to_csv('merged_data.csv', index=False)

# Create an instance of the Pipeline class
pipeline_instance = Pipeline()

# Run the pipeline
pipeline_instance.initialize_pipeline()
"

# Check if the output file exists
check_file_exists "merged_data.csv"

