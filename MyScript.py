#!/usr/bin/env python
import pika
import sys
import sys, json

# Load the data that PHP sent us
data = json.loads(sys.argv[1])
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='52.89.105.19'))
channel = connection.channel()

channel.queue_declare(queue='damperQueue', durable=True)

message = ' '.join(sys.argv[1:]) or data
channel.basic_publish(exchange='',
                      routing_key='damperQueue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()

# Generate some data to send to PHP
result = {'status': 'Yes!'}

# Send it to stdout (to PHP)
print json.dumps(result)




