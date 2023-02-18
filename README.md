# Playing with github actions
## 0. Why
Пробуем создать свой CI/CD пайплайн для домашнего проекта при помощи Python и GitHub Actions<br/>


## 1. Requirements
Для запуска этого проекта потребуется:
- VPS/VDS/VM с *nix ОС, куда будут деплоится контейнеры (проверено на Ubuntu Server 18.04)
- Белый IP адрес (проброшеный порт, иной способ получения веб хука)
- Python 3.8
- Docker
- git
## 2. Get Started
#####Установка серверной части на чистой Ubuntu Server 18.04
```shell script
sudo apt update
git clone https://github.com/AlexTaynov/actions_ci_example.git
cd actions_ci_example/ci_app/
sudo apt install python3-pip
sudo python3 setup.py install
sudo cp ../cd_web_server.service /etc/systemd/system/cd_web_server.service
 # dont forget to add token in cd_web_server.service
sudo systemctl daemon-reload
sudo systemctl enable cd_web_server.service
sudo systemctl start cd_web_server.service
```

Проверить то что веб сервер запустился и работает можно с помощью команд
```shell script
sudo systemctl status cd_web_server.service
```
или
```shell script
curl 0.0.0.0:5555
```

