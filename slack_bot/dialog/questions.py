OVERALL = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hello <@user>! It's time for Content mentoring/production daily report. Please share what you've been working on."
            }
        }
    ]
}

YESTERDAY = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Yesterday's progress"
            }
        }
    ]
}


TODAY = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Plans for today"
            }
        }
    ]
}

BLOCKERS = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Any blockers?"
            }
        }
    ]
}

BLOCKER_BLOCK = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ">*Blockers*\n"
            }
        }

REPORT_TEMPLATE = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "New daily update"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ">*Yesterday Progress*\n"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ">*Today plans*\n"
            }
        },
    ]
}


EDIT_BUTTON = {
    "blocks": [
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Thanks for submission. If you forgot something, you can edit your report."
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Edit report"
                },
                "value": "edit-report",
                "action_id": "edit-action"
            }
        }
    ]
}
