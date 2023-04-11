from slack_bot.dialog.temp_blocks import BLOCKERS, PLANS, PROGRESS, OVERALL
from slack_bot.dialog.interactive import MODAL
from copy import deepcopy


def greet_user(say, username):
    say(f"Hello <@{username}>. It's time for daily report. Please share what you've been working on.")
    response = say("Yesterday's progress?")
    return response['ts']


def format_submission(submission):
    raw_text = submission.split('\n')
    return ''.join([f'\n>{string}' for string in raw_text])


def format_template(template, data, type):
    ready_template = deepcopy(template)
    match type:
        case 'overall':
            greet_msg = f"<@{data}> posted daily update"
            ready_template['text']['text'] = greet_msg
        case _:
            ready_template['text']['text'] += format_submission(data)
    return ready_template


def make_report(current_report):
    report = {'blocks': []}

    overall = format_template(OVERALL, current_report.user_id, 'overall')
    report['blocks'].append(overall)

    progress = format_template(PROGRESS, current_report.progress, 'progress')
    report['blocks'].append(progress)

    plans = format_template(PLANS, current_report.plans, 'plans')
    report['blocks'].append(plans)

    if current_report.blockers:
        blockers = format_template(BLOCKERS, current_report.blockers, 'blockers')
        report['blocks'].append(blockers)
    return report


def prepare_modal(report_info):
    progress, plans, blockers = report_info
    prepared_modal = deepcopy(MODAL)

    prepared_modal['blocks'][0]['element']['initial_value'] = progress
    prepared_modal['blocks'][1]['element']['initial_value'] = plans
    prepared_modal['blocks'][2]['element']['initial_value'] = blockers

    return prepared_modal
