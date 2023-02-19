import datetime


today = datetime.datetime.now()

micro_drop = today.replace(microsecond=0)

print(micro_drop)
#without microseconds