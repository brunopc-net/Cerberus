from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'


def get_today():
    return datetime.today().strftime(DATE_FORMAT)
