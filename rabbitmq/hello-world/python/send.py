#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# create the recipient queue
channel.queue_declare(queue='hello')

# publish the message to the exchange
channel.basic_publish(exchange='',routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()