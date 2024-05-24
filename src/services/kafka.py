from kafka import KafkaProducer, KafkaConsumer
import time
import json
import pandas as pd
import logging as log

log.basicConfig(level=log.INFO)

def kafka_producer(df : pd.DataFrame, topic : str) -> None:
    """
    Send a pandas dataframe to a Kafka topic.

    Parameters:
        df (pd.DataFrame): The DataFrame to be sent to Kafka.

    Returns:
        None
    """
    try:
        log.info('Initiating Kafka producer...')

        producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        for index, row in df.iterrows():
            dict_row = dict(row)
            json_row = json.dumps(dict_row)
            producer.send(topic, value=json_row)
            time.sleep(0.2)
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            log.info(f'Message sent at {formatted_time}')
        
        producer.close()

        log.info('All messages sent')
    
    except Exception as e:
        log.error(f'An error occurred: {e}')

def kafka_consumer(topic: str) -> None:
    """
    Consume data from a Kafka topic and send each message to an API.

    Parameters:
        topic (str): The Kafka topic to consume data from.
    """
    try:
        log.info('Starting consumer...')
        consumer = KafkaConsumer(topic,
                                bootstrap_servers='localhost:9092',
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                consumer_timeout_ms=10000,
                                auto_offset_reset='earliest',
                                enable_auto_commit=True)

        captured_data = []

        for message in consumer:
            data = message.value
            captured_data.append(data)
            offset = message.offset
            log.info(f'Message received successfully in offset: {offset}')

        return captured_data
        log.info('No more data, closing consumer')
    
    except Exception as e:
        log.error(f'An error occurred: {e}')
