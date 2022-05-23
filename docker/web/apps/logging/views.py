from datetime import datetime

from .models import WS


def log(username, app, message):
    timestamp = datetime.now()
    WS.objects.create(username=username, timestamp=timestamp, message=message, app=app)
    return
