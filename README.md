## knativeafka

knativekafka is a wrapper around kafka-python package. This package is easy to use and can be used to test the Kafka Producer in kafka-python package.

Some important items to note.

* This package includes the basic testing only as of now.

*  Polling, parallelism etc. has not been included yet.

### Installation Instructions

The package is availble in PyPI which is an official repository for python package.
pip is a package management system and is used for installing Python packages from Python Package Index (also known as PyPI). It is the most common way to install Python packages.
Install the package in your environment from the terminal using the below pip command:

`pip install knativekafka`


Optionally, you can clone this project by running 

`git clone https://github.com/ezhil-g/knativekafka`

### Pre-requisites

- Python 3.x

- pip3

- Set the environment variables - KAFKA_BROKERS and TOPIC.


### How to Use?

* Import the Kafka Producer into your python code using the below import.

`from knativekafka.knativekafkaproducer import KNativeKafkaProducer`

To import the Kafka Consumer use the below import.
`from knativekafka.knativekafkaconsumer import KNativeKafkaConsumer`
    

#### Usage

Only few features are implemented in the package as of now. 

If you want any additional features implemented, feel free to modify the repo.

#### Test Producer

To test the producer, perform the below steps.

* Instantiate the KNativeKafkaProducer and then, call send_binary_data(). The send_binary_data() takes the message in binary format.

```
kafka_producer = KNativeKafkaProducer(os.environ['KAFKA_BROKERS'],os.environ['TOPIC'])
value = input('value:')
value = bytes(value, encoding='utf8')            
kafka_producer.send_binary_data(value)    

```

### License

```
Apache License
```
