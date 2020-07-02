import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'share.settings')
django.setup()

from proxy.action import GetFreeProxy
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time


def test_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)


def get_proxy_task():
    proxy_obj = GetFreeProxy()
    proxy_obj.pool_task()


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_proxy_task, 'date', run_date='2020-07-02 22:58:00')
    scheduler.start()
    while True:
        pass









