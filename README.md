# Readme
Init project for a telegram bot, it has basic functionalities and modules.

### Instructions
Assuming you have already installed Heroku and created a bot from `BotFather`
```
heroku create <HEROKU_APP_NAME>
heroku config:set TOKEN=<YOUR_TOKEN>
```
With this, you are ready to start your own bot. You can also add environment variables on the dashboard of your app (Settings > Config variables)

#### Adding Postgres :elephant:

```
heroku addons:create heroku-postgresql
```
Enter to [Heroku](www.heroku.com) to get the environment variables you need (Your app > Resources > Heroku Postgres :: Database > Settings > Database credentials)

If you want to access your database, you can do it with the following command:
```
heroku pg:psql
```

Project based on previous one made in collaboration of [Cristián Cortés](https://github.com/criscv94)
