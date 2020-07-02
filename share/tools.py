import time
from datetime import datetime, timedelta
import random


class Tools(object):
    def __init__(self):
        pass

    @staticmethod
    def format_p2s_time1(p_time):
        return datetime.strftime(p_time, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def format_p2s_time2(p_time):
        return datetime.strftime(p_time, '%Y-%m-%d %H:%M')

    @staticmethod
    def format_p2s_time3(p_time):
        return datetime.strftime(p_time, '%Y-%m-%d')

    @staticmethod
    def format_s2p_time1(s_time):
        return datetime.strptime(s_time, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def format_s2p_time2(s_time):
        return datetime.strptime(s_time, '%Y-%m-%d %H:%M')

    @staticmethod
    def format_s2p_time3(s_time):
        return datetime.strptime(s_time, '%Y-%m-%d')

    @staticmethod
    def get_new_time(p_time, number, flag='s'):
        new_time = p_time
        if flag == 's':
            new_time = p_time + timedelta(seconds=number)
        if flag == 'm':
            new_time = p_time + timedelta(minutes=number)
        if flag == 'h':
            new_time = p_time + timedelta(hours=number)
        if flag == 'd':
            new_time = p_time + timedelta(days=number)
        return new_time

    @staticmethod
    def sleep_time(*args):
        length = len(args)
        if length == 1:
            time.sleep(args[0])
        if length == 2:
            if args[1] > args[0]:
                time.sleep(random.randint(args[0], args[1]))
            else:
                time.sleep(random.randint(args[1], args[0]))


