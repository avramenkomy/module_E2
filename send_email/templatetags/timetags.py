from django import template
import datetime
register = template.Library()

def print_timestamp(time_obj):
    try:
        ts = datetime.datetime.timestamp(time_obj)
    except ValueError:
        return None
    return ts

def sub(obj1, obj2):
    try:
        ts1 = float(obj1)
        ts2 = obj2.timestamp()
    except ValueError:
        return None
    return ts1 - ts2


register.filter(print_timestamp)
register.filter(sub)