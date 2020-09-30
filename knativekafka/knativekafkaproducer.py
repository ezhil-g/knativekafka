import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import threading
import logging

class KNativeKafkaProducer(threading.Thread):
    daemon = True

    def __init__(self, server, topic):
        """Initialize using the params
           :param self: KNativeKafkaProducer object           
           :param server: Kafka bootstrap server      
           :param topic: Kafka topic name
        """
        self.logger = logging.getLogger()
        self.logger.info("Initializing Kafka Producer")
        self.producer = KafkaProducer(bootstrap_servers=server)
        self.topic = topic

    def send_binary_data(self, data:str):
        """Sends the binary data to Kafka topic using the send()
            :param self: KNativeKafkaProducer object
            :param data: A string representing of binary message          
            :return: Message value gets returned
            
        """
        try:
            self.logger.info('Sending the data {} to topic {}'.format(data, self.topic))
            self.producer.send(self.topic, data)
            self.producer.flush(30)
        except KafkaError as e:
            self.logger.error(f'Kafka Error {e}')
            raise Exception(f'Kafka Error {e}')
    
  



