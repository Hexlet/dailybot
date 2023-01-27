import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

from dialog.interactive import MODAL, EDIT_BUTTON
from utils import make_report
from user_controller import User, storage

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot_token = os.environ["SLACK_BOT_TOKEN"]
app_token = os.environ["SLACK_APP_TOKEN"]

app = App(token=bot_token)


@app.event('message')
def handle_message(ack, say, message):
    ack()
    user_id = message['user']
    user_message_ts = message['ts']
    current_user = storage.get(user_id, None)
    message_content = message['text']
    if current_user and current_user.latest_part != 'full report':

        if current_user.is_newer_message(user_message_ts):
            current_user.save_report_part(message_content)
            latest = current_user.latest_part

            if latest == 'progress':
                response = say("Today plans?")
                current_user.save_ts(response['ts'], 'question')

            elif latest == 'plans':
                response = say("Blockers?")
                current_user.save_ts(response['ts'], 'question')

            elif latest == 'full report':
                report = make_report(current_user)
                logging.info(f'{current_user.username} send report: ', report)
                response = say(text=report, channel='C04FEM741BR')
                say(text=EDIT_BUTTON)
                current_user.save_ts(response['ts'], 'question')
                current_user.save_ts(response['ts'], 'report')

    # elif message['thread_ts'] == current_user.report_ts:
    #     say(
    #         f"Hey, <@{current_user.username}>! You've got new reply.",
    #         thread_ts=message['thread_ts']
    #         )


@app.command('/report')
def handle_report_command(ack, command, say):
    ack()

    user_id = command['user_id']
    current_user = User(user_id)
    storage[user_id] = current_user

    username = command['user_name']
    current_user.set_username(username)

    say(f"Hello <@{username}>. It's time for daily report. Please share what you've been working on.")
    response = say("Yesterday's progress?")
    current_user.save_ts(response['ts'], 'question')


@app.action('edit-action')
def call_edit_modal(ack, client, body, action):
    ack()
    logging.info(client.views_open(
        trigger_id=body["trigger_id"],
        view=MODAL
    ))


@app.view("view-id")
def edit_report(ack, body, say, view, response):
    ack()


@app.message('test')
def handle_test_message(ack, say):
    ack()
    say(text='Ok. This is test.')

# @app.view("view-id")
# def view_submission(ack, body, say, view, response):
#     ack()
#     current_report['report'] = view
#     user_id = get_user_id(body)
#     greet_msg = get_greet_msg(body)
#     yesterday_progress = get_report_details(view, 'progress')
#     today_plans = get_report_details(view, 'plans')
#     blockers = get_report_details(view, 'blockers')
#     report = fill_report(greet_msg, yesterday_progress, today_plans, blockers)
#     response = say(text=report, channel='C04FEM741BR')
#     current_report['ts'] = response['ts']

#     say(text=EDIT_BUTTON, channel=user_id)


if __name__ == "__main__":
    SocketModeHandler(app, app_token).start()
