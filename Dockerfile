FROM --platform=linux/amd64 python:3.9-slim-buster

WORKDIR /

COPY ./app .

RUN apt-get update && pip install --no-cache-dir -r requirements.txt

EXPOSE 5500

CMD ["python", "app.py"]
