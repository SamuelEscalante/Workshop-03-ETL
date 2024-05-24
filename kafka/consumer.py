# Work directory setup
# ======================================================================
import sys
import os

work_dir = os.getenv("WORK_DIR")
sys.path.append(work_dir)

# Modules Functions
# ======================================================================
from src.services.kafka import kafka_consumer
from src.database.database_functions import get_engine, create_table, insert_data
from src.models.database_models import Model

# Libraries
# ======================================================================
import joblib
import pandas as pd
import json


if __name__ == '__main__':

    msgs_consumer = kafka_consumer('world_happiness')

    msgs_consumer = [json.loads(data) for data in msgs_consumer]
    df = pd.json_normalize(msgs_consumer)

    model = joblib.load('../ml_model/gbr_model.pkl')
    df_model = df.drop(columns=['Happiness_Score', 'id'], axis=1)
    predictions = model.predict(df_model)
    df['Predicted_Happiness_Score'] = predictions

    column_order = ['id', 'Social_Support', 'Year', 'Trust', 'Generosity','Health', 'Economy', 'Freedom', 'Continent_Africa', 'Continent_Asia', 'Continent_Europe', 'Continent_North_America', 'Continent_Oceania', 'Continent_South_America', 'Economy_Health', 'Trust_Freedom', 'Economy_Trust','Trust_Health', 'Happiness_Score','Predicted_Happiness_Score']
    df = df[column_order]

    connection = get_engine()

    create_table(connection, Model, 'ml_model')
    insert_data (df, 'ml_model', connection)
