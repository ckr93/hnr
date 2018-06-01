from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

war_start = '2011.01.03'
currrent_data =  '2018.03.01'
a = war_start.replace(".", "")
b = currrent_data.replace(".", "")
print(a)
print(b)
x = datetime.strptime(a, "%Y%m%d").date()
y = datetime.strptime(b, "%Y%m%d").date()
print(x)
print(y)

g = x + relativedelta(years=+2)
difference_in_years = relativedelta(x, y).years
print(difference_in_years)

r = g.strftime('%m/%d/%Y')
e = str(r)
print(e)
print(r)





