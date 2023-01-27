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

MODAL = {
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
}
