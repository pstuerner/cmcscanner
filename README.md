# CMCScanner
A small application to query the CoinMarketCap API and store up-to-date listings in a MongoDB.

### How to use it
1. Clone the repo `git clone https://github.com/pstuerner/cmcscanner.git`
2. Edit the `.env` file for your MongoDB and CoinMarketCap credentials
3. Run `docker-compose up -d` to start the application and database

### How it works
The docker-compose starts two services: a simple Python application to send requests to the CoinMarketCap API and a MongoDB instance to store the received results. The Python container includes a cronjob that fires every day at 8am UTC. Feel free the change the [crontab](https://github.com/pstuerner/cmcscanner/blob/master/crontab) if you want to have a different schedule.
It's tricky to let cron use the container's environment variables. I solved it using the following two files: [job.sh](https://github.com/pstuerner/cmcscanner/blob/master/app/job.sh), [start.sh](https://github.com/pstuerner/cmcscanner/blob/master/app/start.sh). Have a look if you're running into the same problem.
The [.env](https://github.com/pstuerner/cmcscanner/blob/master/.env) file includes everything the MongoDB needs to create a root and developer user as well as a name for your database. Pay attention to the [init-mongo.sh](https://github.com/pstuerner/cmcscanner/blob/master/init-mongo.sh) file if you want to know how to create a default user and database during container start. The last thing required is your CoinMarketCap API key that also goes into the .env file.
