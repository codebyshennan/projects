#!/usr/bin/env python
import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# create the recipient queue (if it doesn't already exist)
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"

# publish the message to the exchange
channel.basic_publish(exchange='',routing_key='hello',
                      body='Hello World!')
print(" [x] Sent %r" % message)

# Close the connection
connection.close()connection.close()