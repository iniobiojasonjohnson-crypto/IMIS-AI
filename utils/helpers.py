from datetime import datetime

def now():

    return datetime.utcnow()

def percentage(part,total):

    if total == 0:

        return 0

    return round((part/total)*100,2)
