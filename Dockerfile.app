FROM ubuntu:latest

COPY requirements.txt .

RUN apt-get -y update \
    && apt-get install -y cron nano python3 python3-pip \
    && touch /var/log/cron.log \
    && pip3 install -r requirements.txt

COPY /app /app
COPY crontab /etc/cron.d/cjob
RUN chmod 0644 /etc/cron.d/cjob
RUN chmod 0644 /app/start.sh && chmod +x /app/start.sh && chmod +x /app/job.sh

WORKDIR /app

CMD ["/app/start.sh"]
