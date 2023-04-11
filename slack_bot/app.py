import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from slack_bot.config import get_config
from slack_bot.services import user_reports, users, messages


logger = logging.getLogger(__name__)

config = get_config()

logging.basicConfig(level=logging.INFO)

app = App(token=config['bot_token'])


@app.message('test')
def handle_test_message(ack, say):
    ack()
    say(text='Ok. This is test.')


@app.command('/report')
def handle_report_command(ack, command, say):
    ack()

    user_id = command['user_id']
    logging.info(f'{user_id} initiated report command')
    username = command['user_name']
    message_ts = messages.greet_user(say, username)
    user = users.get_user(user_id)
    if not user:
        users.create_user(user_id, username)
    report = user_reports.create_user_report(
        user_id, message_ts
    )
    logging.info(f'Created new report: {report}')


@app.event('message')
def handle_message(ack, say, message):
    ack()
    user_id = message['user']
    user_message_ts = message['ts']
    logging.info(user_message_ts)
    message_content = message['text']

    current_report = user_reports.get_latest_report(user_id)
    if not current_report.is_completed():

        if current_report.is_newer_message(user_message_ts):

            current_report = user_reports.save_report_part(
                current_report, message_content
            )
            message = current_report.get_message()
            response = say(message)
            user_reports.update_timestamp(
                current_report, response['ts'], 'question'
            )

    if current_report.is_completed():
        report_info = user_reports.get_latest_report(user_id).info
        logging.info(report_info)
        report = messages.make_report(current_report)
        logging.info(f'{user_id} succesfully send report')
        response = say(text=report, channel='C051H1BCZ7U')
        user_reports.update_timestamp(
            current_report, response['ts'], 'question'
        )
        user_reports.update_timestamp(
            current_report, response['ts'], 'report'
        )


@app.action('edit-action')
def call_edit_modal(ack, client, body):
    ack()
    user_id = body['user']['id']
    report = user_reports.get_latest_report(user_id)
    report_info = report.info
    prepared_modal = messages.prepare_modal(report_info)
    client.views_open(
        trigger_id=body["trigger_id"],
        view=prepared_modal
    )


@app.view("view-id")
def edit_report(ack, body, say, view, response):
    ack()


if __name__ == "__main__":
    SocketModeHandler(app, config['app_token']).start()
