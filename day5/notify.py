# give notification daily

from plyer import notification
import datetime

def sendnot():
    now = datetime.datetime.now().strftime("18:00:00")
    notification.notify(
        title="⏰ TIME TO FUN",
        message=f"Hey Ankit! It's {now}. Time to close  your Python lecture! 💻",
        timeout=10
    )

sendnot()