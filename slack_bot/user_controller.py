STOP_WORDS = ['no', 'none', '-', 'нет']


class User:
    username = None
    group_id = None
    progress = None
    plans = None
    blockers = None
    report_ts = None
    question_ts = None
    report_chat_id = None
    latest_part = None

    def __init__(self, user_id):
        self.user_id = user_id

    def _is_blockers(self, report_part):
        return False if report_part in STOP_WORDS else True

    def set_username(self, username):
        self.username = username

    def save_report_part(self, report_part):
        match self.latest_part:
            case None:
                self.progress = report_part
                self.latest_part = 'progress'

            case 'progress':
                self.plans = report_part
                self.latest_part = 'plans'

            case 'plans':
                self.blockers = report_part if self._is_blockers(report_part) else None
                self.latest_part = 'full report'

            case 'full report':
                pass

    def save_ts(self, ts, type):
        match type:
            case 'report':
                self.report_ts = ts

            case 'question':
                self.question_ts = ts

    def set_chat_to_report(self, chat_id):
        self.report_chat_id = chat_id

    def is_newer_message(self, message_ts):
        return self.question_ts < message_ts
