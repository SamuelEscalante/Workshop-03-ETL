# Data Handling
# ======================================================================
import pandas as pd

# Modules Functions
# ======================================================================
from utils.years_functions import *
from src.services.kafka import kafka_producer

# Logging and Event Handling
# ======================================================================
import logging as log

# Serialization and Deserialization
# ======================================================================
import json

# Time Handling
# ======================================================================
import time

# Machine Learning
# ======================================================================
from sklearn.model_selection import train_test_split


log.basicConfig(level=log.INFO)

def feature_selection() -> pd.DataFrame:
    """
    Perform feature selection for a DataFrame.

    Parameters:
    ----------
        df (pd.DataFrame): The DataFrame to perform feature selection on.

    Returns:
    ----------
        pd.DataFrame: The DataFrame with selected features.
    """
    try:
        # Load Datasets
        # ======================================================================
        data = load_datasets('../data')

        df_2015 = data[2015]
        df_2016 = data[2016]
        df_2017 = data[2017]
        df_2018 = data[2018]
        df_2019 = data[2019]

        # Data Cleaning
        # ======================================================================
        df_2018 = df_2018.dropna()

        # Data Transformation
        # ======================================================================
        normalize_columns = normalize_column_names({2015: df_2015, 2016: df_2016, 2017: df_2017, 2018: df_2018, 2019: df_2019})
        year_column = add_year_column(normalize_columns)

        df_2015 = normalize_columns[2015]
        df_2016 = normalize_columns[2016]
        df_2017 = normalize_columns[2017]
        df_2018 = normalize_columns[2018]
        df_2019 = normalize_columns[2019]

        # Concatenate DataFrames
        # ======================================================================

        concatenated_df = concatenate_common_columns({2015: df_2015, 2016: df_2016, 2017: df_2017, 2018: df_2018, 2019: df_2019})

        # Concatenate DataFrame Transformation
        # ======================================================================

        concatenated_df = map_country_to_continent(concatenated_df)

        concatenated_df = pd.get_dummies(concatenated_df, columns=['Continent'] ,dtype=int)
        concatenated_df.drop(columns=['Country', 'Happiness_Rank'], axis=1, inplace=True)

        new_columns = {
            'Continent_North America' : 'Continent_North_America',
            'Continent_South America' : 'Continent_South_America'
        }

        concatenated_df.rename(columns=new_columns, inplace=True)

        # Add interactions between columns
        # ======================================================================

        concatenated_df['Economy_Health'] = concatenated_df['Economy'] * concatenated_df['Health']
        concatenated_df['Trust_Freedom'] = concatenated_df['Trust'] * concatenated_df['Freedom']
        concatenated_df['Economy_Trust'] = concatenated_df['Economy'] * concatenated_df['Trust']
        concatenated_df['Trust_Health'] = concatenated_df['Trust'] * concatenated_df['Health']

        # Test Split
        # ======================================================================

        X = concatenated_df.drop(columns=['Happiness_Score'], axis=1)
        y = concatenated_df['Happiness_Score']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=52)

        log.info('Data Preprocessing Completed')

        log.info('Performing some transformations on the data...')
        X_test['Happiness_Score'] = y_test
        X_test.insert(0, 'id', X_test.index + 1)
        column_order = ['id', 'Social_Support', 'Year', 'Trust', 'Generosity','Health', 'Economy', 'Freedom', 'Happiness_Score', 'Continent_Africa', 'Continent_Asia', 'Continent_Europe', 'Continent_North_America', 'Continent_Oceania', 'Continent_South_America', 'Economy_Health', 'Trust_Freedom', 'Economy_Trust','Trust_Health']
        X_test = X_test[column_order]

        log.info('Data transformations completed')
        return X_test
    
    except Exception as e:
        log.error(f'An error occurred: {e}')