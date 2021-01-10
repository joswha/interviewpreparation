from datetime import datetime, timedelta

def add(moment):
    return moment + timedelta(seconds = 10 ** 9 )
print(add(datetime(2015, 1, 24, 22, 0)))