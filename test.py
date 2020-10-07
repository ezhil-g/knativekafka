
from knativekafka.knativekafkaproducer import KNativeKafkaProducer
from knativekafka.knativekafkaconsumer import KNativeKafkaConsumer
import logging
import os
import sys

def main():

    try:
    
        print("Let's initialize the kafka server....")

        topic =  "python-topic"
        os.environ['KAFKA_BOOTSTRAP_SERVERS'] = 'localhost:9092'
        
        print(os.environ.get('KAFKA_BOOTSTRAP_SERVERS'))
        kafka_producer = KNativeKafkaProducer(topic)
        value = input('value:')
        value = bytes(value, encoding='utf8')            
        kafka_producer.send_binary_data(value)    
        print("Successfully sent data....")
        kafka_consumer =  KNativeKafkaConsumer(topic)
        kafka_consumer.getMessage()
        print("Successfully got data....")
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")

if __name__ == "__main__":
    main()