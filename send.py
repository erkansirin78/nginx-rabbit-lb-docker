import pika, time, random
credentials = pika.PlainCredentials(username='guest', password='guest')
conn_params = pika.ConnectionParameters(host='localhost', port=15000, credentials=credentials)
connection = pika.BlockingConnection(conn_params)

channel = connection.channel(channel_number=3)

channel.queue_declare(queue='hello')

for i in range(1,2000):
    st = random.uniform(0, 1)
    print(st, i)
    time.sleep(st)
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World! - ' + str(i))


    print(" [x] 'Hello World!'", i)

connection.close()
