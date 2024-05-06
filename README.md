# asya-bot-diploma

### Установка через Docker Compose
`docker-compose up -d`

### Удаление через Docker Compose
`docker-compose down`

### Установка через Dockerfile
`sudo docker build -t asya-bot-diploma .`
`sudo docker run --restart always asya-bot-diploma`  

### Удаление через Dockerfile
`docker stop $(docker ps -q)`  
`docker rm $(docker ps -a -q)`  
`docker rmi $(docker images -q)`  

### ТОКЕНЫ в .env
`Нужен токен для бота`   
`Нужен токен для 2ГИС`  

### Обновление venv
`pip freeze > 1.txt && pip uninstall -y -r 1.txt && pip install --no-cache-dir -r requirements.txt && rm 1.txt`  
