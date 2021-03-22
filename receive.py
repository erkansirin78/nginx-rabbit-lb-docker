import pika, time

credentials = pika.PlainCredentials(username='guest', password='guest')
conn_params = pika.ConnectionParameters(host='localhost', port=15000, credentials=credentials)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel(channel_number=4)
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print("[x] Received %r" % body)

channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for the messages. To exit press Ctrl+C')
channel.start_consuming()
