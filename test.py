
from knativekafka.knativekafkaproducer import KNativeKafkaProducer
from knativekafka.knativekafkaconsumer import KNativeKafkaConsumer
import logging
import os
import sys

def main():

    try:
    
        print("Let's initialize the kafka server....")
        os.environ['KAFKA_BROKERS']='xxx'
        os.environ['TOPIC']="python-kafka-topic"
        kafka_producer = KNativeKafkaProducer(os.environ['KAFKA_BROKERS'],os.environ['TOPIC'])
        value = input('value:')
        value = bytes(value, encoding='utf8')            
        kafka_producer.send_binary_data(value)    
        print("Successfully sent data....")
        kafka_consumer =  KNativeKafkaConsumer(os.environ['KAFKA_BROKERS'],os.environ['TOPIC'])
        msg = kafka_consumer.getMessage()
        print("Successfully got data....")
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
    except Exception:
        print(e)

if __name__ == "__main__":
    main()