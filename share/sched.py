import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share.settings')
django.setup()


from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime
import time


def test_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)


# if __name__ == "__main__":
scheduler = BlockingScheduler()
# while True:
scheduler.add_job(test_task, 'interval', seconds=2)
scheduler.start()









