# asya-bot-diploma

### Установка через Docker Compose c мониторингом
`sudo docker-compose up -d`

### Удаление через Docker Compose
`sudo docker-compose down`

### Установка через Dockerfile
`sudo docker build -t asya-bot-diploma .`
`sudo docker run --restart always asya-bot-diploma`  

### Удаление через Dockerfile
`sudo docker stop $(sudo docker ps -q)`  
`sudo docker rm $(sudo docker ps -a -q)`  
`sudo docker rmi $(sudo docker images -q)`  

### ТОКЕНЫ в .env
`Нужен токен для бота`   
`Нужен токен для 2ГИС`  

`Пример файла:`  
```
BOT_TOKEN=****
MAP_TOKEN=****
AI_TOKEN=****
```

### Обновление venv
`pip freeze > 1.txt && pip uninstall -y -r 1.txt && pip install --no-cache-dir -r requirements.txt && rm 1.txt`  
