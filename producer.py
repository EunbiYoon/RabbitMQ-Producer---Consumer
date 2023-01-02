import pika

# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#declare queue
channel.queue_declare(queue='letterbox')

#message
message="Hello this is my first message"
channel.basic_publish(exchange='',routing_key='letterbox',body=message)

#check
print(f"sent message :{message}")

#close connection
connection.close()

