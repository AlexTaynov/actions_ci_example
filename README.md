# Playing with github actions
## 0. Why
Пробуем создать свой CI/CD пайплайн для домашнего проекта при помощи Python и GitHub Actions<br/>


## 1. Requirements
Для запуска этого проекта потребуется:
- VPS/VDS/VM с *nix ОС, куда будут деплоится контейнеры (проверено на Ubuntu Server 18.04)
- Белый IP адрес (проброшеный порт, иной способ получения веб хука)
- Docker
## 2. Get Started
Установка серверной части
```shell script
docker build -t $(IMAGE_NAME) -f Dockerfile .
docker run --name deploy_server -p 5500:5500 -v /var/run/docker.sock:/var/run/docker.sock -d -e CI_TOKEN=<I generate it with $(openssl rand -hex 20)> --restart=always $(IMAGE_NAME)
```

Проверить то что веб сервер запустился и работает можно с помощью команды
```shell script
curl 0.0.0.0:5555
```

