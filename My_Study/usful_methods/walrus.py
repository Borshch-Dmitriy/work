# :=
from datetime import date
print(date(year:=int(input()),month:=int(input()),int(*(21 + i for i in range(1,8) if date(year,month,i).isoweekday() == 4))).strftime("%d.%m.%Y"))



