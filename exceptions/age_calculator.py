from datetime import datetime
from dateutil import relativedelta

# get two dates
d1 = '2000-2-29'
# d2 = '27-11-2023'
d2=str(datetime.today().date())
print(d2)
# convert string to date object
# start_date = datetime.strptime(d1, "%d-%m-%Y")
# end_date = datetime.strptime(d2, "%d-%m-%Y")


start_date = datetime.strptime(d1, "%Y-%m-%d")
end_date = datetime.strptime(d2, "%Y-%m-%d")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print('Years, Months, Days between two dates is')
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')