from kafka import KafkaProducer
import json
from data import get_registered_user
import time


def json_serializer(data):  # Proper indentation for the function body
    """Serializes data as JSON-encoded bytes."""
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=json_serializer)

if __name__ == "__main__":
    while True:  # Using True for infinite loop (more Pythonic)
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)
