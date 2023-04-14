# hexlet-dailybot

hexlet-dailybot is bot for Slack designed to request a daily report.

## Requirements

- python = "^3.8.1"
- slack-bolt = "^1.16.1"

## Installation

1. Fork repo
2. Clone forked repo

    ```bash
    git clone git@github.com:<your-git-account>/dailybot.git
    ```

3. Create workspace for development in [Slack](https://slack.com/help/articles/206845317-Create-a-Slack-workspace)
4. In workspace go to "Settings & administration" -> "Manage apps". Press "Create new app" -> "From scratch". Enter any name in "App Name" field and select workspace created by you
5. Select socket mode and create app-level token. Copy created token in .env file
6. Add slash commands - currently we use only `/report`
7. In `OAuth & Permissions` press install to workspace button. Copy `Bot User OAuth Token` in .env file
8. Select needed capabilities and permissions for bot scopes
9. Select `Enable Events` in `Event Subscriptions`

### Poetry

- Run `make install`
- Run `make start`

### Docker

- Run `make docker-build`
- Run `make docker-start`

### Deploy to Railway

1. Choose forked repo. Create database PostgreSQL.
2. In created app specify variables from database and tokens from slack
3. In app settings specify start command - `make migrate && make start`
4. Verify the logs to make sure the application is successfully deployed
