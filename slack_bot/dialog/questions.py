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
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ">*Blockers*\n"
            }
        }
    ]
}
