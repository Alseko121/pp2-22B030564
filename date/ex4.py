import datetime

today = datetime.datetime.now()

one_year_ago = today - datetime.timedelta(days=365)

difference = (today - one_year_ago).days

result = f" {one_year_ago:%Y-%m-%d} and {today:%Y-%m-%d} is {difference:,} days."

print(result)
#difference two data