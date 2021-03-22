# nginx-rabbit-lb-docker
Using Nginx as load balancer with rabbitmq cluster

You might need to use nginx as load balancer in front of rabbitmq cluster for several reason. In this project I used docker-compose using official nginx and rabbitmq images. 

```
git clone 
https://github.com/erkansirin78/nginx-rabbit-lb-docker.git
cd nginx-rabbit-lb-docker
docker-compose up -d
```

Wait for a while then open up browser and http://localhost:15672/

## Via rabbitmq original port
![Rabbitmq management we ui](rabbitmq_management_ui_localhost.jpg "Rabbitmq management we ui")

## Via Nginx
![Rabbitmq management we ui via nginx](rabbitmq_management_ui_via_nginx.jpg "Rabbitmq management we ui  via nginx")
