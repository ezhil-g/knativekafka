# Serialize json messages
import json
import logging
import base64
import os
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import threading

import time

class KNativeKafkaConsumer(threading.Thread):
    daemon = True    

    def __init__(self, server, topic):
        """Initialize using the params
           :param self: KNativeKafkaConsumer object           
           :param server: Kafka bootstrap server      
           :param topic: Kafka topic name
        """
        self.logger = logging.getLogger()
        self.logger.info("Initializing Kafka Consumer")
        self.consumer = KafkaConsumer(bootstrap_servers=server,
                            auto_offset_reset='earliest',
                            value_deserializer=bytes.decode)
        self.topic = topic
    def getMessage(self) -> str:
        """Get the message
            :param self: KNativeKafkaConsumer object           
            :param server: Kafka bootstrap server      
            :param topic: Kafka topic name                   
            :return: none
        """
        print("**** Print the Messages ****")
        self.consumer.subscribe([self.topic])
        for message in self.consumer:
            print("topic={} partition={} offset={} key={} value={}".format(message.topic,
                                                                        message.partition,
                                                                        message.offset,
                                                                        message.key,
                                                                        message.value))
        return message.value
                


        
