# asya-bot-diploma

### Установка
sudo docker build -t asya-bot-diploma .  
sudo docker run --restart always asya-bot-diploma

### Удаление
docker stop $(docker ps -q)  
docker rm $(docker ps -a -q)  
docker rmi $(docker images -q)  

### ТОКЕНЫ в .env
Нужен токен для бота  
Нужен токен для 2ГИС  
