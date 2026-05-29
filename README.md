Запустите скрипт из папки репозитория:

cd ./backend;  docker build -f Dockerfile .  -t python-server-em:0.1; cd ../nginx/; docker build -f Dockerfile .  -t nginx-em:0.1

он соберет нужные образы

далее запустите docker-compose.yml:

docker-compose -f docker-compose.yml up -d 

Проверка:
зайти на localhost или 127.0.0.1 по 80 порту через браузер или curl


как работает:

пользователь -> nginx reverse proxy на 80 порту -> сервер на питоне на 8080
