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

3. Specify environment variables in `.env.example`. [Where to find tokens](https://api.slack.com/authentication/token-types#bot).

### Poetry

- Run `make install`
- Run `make start`

### Docker

- Run `make docker-build`
- Run `make docker-start`
