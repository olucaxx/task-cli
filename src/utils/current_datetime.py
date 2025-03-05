import datetime

def get_current_datetime() -> str:
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
