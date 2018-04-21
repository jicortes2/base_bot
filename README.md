# Readme
Init project for a telegram bot, it has basic functionalities and modules.

### Instructions
Assuming you have already installed Heroku and create a bot from `BotFather`
```
heroku create <HEROKU_APP_NAME>
heroku config:set TOKEN=<YOUR_TOKEN>
```
With this, you are ready to start your own bot.

##### Adding postgres
```
heroku addons:create heroku-postgresql
```
Enter to [Heroku](www.heroku.com) to get the environment variables you need (Your app > Resources > Heroku Postgres :: Database > Settings > Database credentials)

If you want to access to your database, you can do it with the following command:
```
heroku pg:psql
```
