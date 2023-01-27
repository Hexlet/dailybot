from dialog.temp_blocks import BLOCKERS, PLANS, PROGRESS, OVERALL
from copy import deepcopy


def format_submission(submission):
    raw_text = submission.split('\n')
    return ''.join([f'\n>{string}' for string in raw_text])


def format_template(template, user, type):
    ready_template = deepcopy(template)
    match type:
        case 'overall':
            greet_msg = f"<@{user.username}> posted daily update"
            ready_template['text']['text'] = greet_msg
        case 'progress':
            ready_template['text']['text'] += format_submission(user.progress)
        case 'plans':
            ready_template['text']['text'] += format_submission(user.plans)
        case 'blockers':
            ready_template['text']['text'] += format_submission(user.blockers)
    return ready_template


def make_report(user):
    report = {'blocks': []}

    overall = format_template(OVERALL, user, 'overall')
    report['blocks'].append(overall)

    progress = format_template(PROGRESS, user, 'progress')
    report['blocks'].append(progress)

    plans = format_template(PLANS, user, 'plans')
    report['blocks'].append(plans)

    if user.blockers:
        blockers = format_template(BLOCKERS, user, 'blockers')
        report['blocks'].append(blockers)
    return report
