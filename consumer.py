import pika

def on_message_received(ch, method, properties, body):
    print(f"received new message :{body}")

# create connection
connection_parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_parameters)

#create channel
channel=connection.channel()

#declare queue
channel.queue_declare(queue='letterbox')

#consume queue
channel.basic_consume(queue='letterbox',auto_ack=True, 
    on_message_callback=on_message_received)

#check
print("Starting Consuming")

channel.start_consuming()