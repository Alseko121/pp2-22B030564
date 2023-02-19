import datetime

today = datetime.datetime.now().date()

five_days = today - datetime.timedelta(days=5)

print("Five days ago:", five_days)
# - 5 days