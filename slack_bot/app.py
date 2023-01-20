import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

from utils import get_username, get_report_details, fill_report

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ["SLACK_APP_TOKEN"]

app = App(token=bot_token)


@app.message('hello')
def greet(say, ack):
    ack()
    say(text='hello there')


@app.event("message")
def say_hello(ack, say, message):
    ack()
    logging.info(message)
    say(f"Hey there <@{message['user']}>!")


@app.command('/report')
def daily_report(body, ack, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view-id",
            "title": {
                "type": "plain_text",
                "text": "Daily report",
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
            },
            "blocks": [
                {
                    "type": "input",
                    "block_id": "progress",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "progress_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Yesterday Progress",
                    },
                },
                {
                    "type": "input",
                    "block_id": "plans",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plans_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Plans for today",
                    },
                },
                {
                    "type": "input",
                    "block_id": "blockers",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "blockers_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Blockers?",
                    },
                },
            ],
        },
    )


@app.view("view-id")
def view_submission(ack, body, say, view, context):
    ack()
    logging.info(body)
    logging.info(context.channel_id)
    username = get_username(body)
    greet_msg = f"<@{username}> posted daily update"
    yesterday_progress = get_report_details(view, 'progress')
    today_plans = get_report_details(view, 'plans')
    blockers = get_report_details(view, 'blockers')

    report = fill_report(greet_msg, yesterday_progress, today_plans, blockers)
    say(text=report, channel='C04FEM741BR')


if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()
