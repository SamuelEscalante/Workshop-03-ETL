# Work directory setup
# ======================================================================
import sys
import os

work_dir = os.getenv("WORK_DIR")
sys.path.append(work_dir)

# Modules Functions
# ======================================================================
from utils.feature_selection_functions import feature_selection
from src.services.kafka import kafka_producer


if __name__ == '__main__':

    df = feature_selection()
    producer = kafka_producer(df, 'world_happiness')

