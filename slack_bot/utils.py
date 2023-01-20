from dialog.questions import REPORT_TEMPLATE, BLOCKER_BLOCK
from copy import deepcopy

BLOCKERS_STOP_WORDS = ['no', 'none', '-', 'нет']


def format_submission(text):
    raw_text = text.split('\n')
    return '\n'.join([f'>{string}' for string in raw_text])


def get_username(body):
    return body['user']['username']


def get_report_details(view, stat):
    return view['state']['values'][f'{stat}'][f'{stat}_input-action']['value']


def fill_report(greet_msg, yesterday_progress, today_plans, blockers):
    report = deepcopy(REPORT_TEMPLATE)
    report["blocks"][0]['text']['text'] = greet_msg
    report['blocks'][1]['text']['text'] += format_submission(yesterday_progress)
    report['blocks'][2]['text']['text'] += format_submission(today_plans)
    if blockers not in BLOCKERS_STOP_WORDS:
        report['blocks'].append(BLOCKER_BLOCK)
        report['blocks'][3]['text']['text'] += format_submission(blockers)
    return report
