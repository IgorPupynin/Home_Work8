from datetime import datetime, timedelta


users = [
    {"name": "Bill1", "birthdate": datetime(year=2022, month=12, day=31)},
    {"name": "Bill2", "birthdate": datetime(year=2023, month=1, day=1)},
    {"name": "Bill3", "birthdate": datetime(year=1800, month=1, day=2)},
    {"name": "Bill4", "birthdate": datetime(year=2022, month=1, day=3)},
    {"name": "Bill5", "birthdate": datetime(year=2023, month=1, day=4)},
    {"name": "Bill6", "birthdate": datetime(year=1800, month=1, day=5)},
    {"name": "Bill7", "birthdate": datetime(year=1800, month=1, day=6)}
]

current_date1 = datetime.now()
current_date = datetime(
    year=2000, month=current_date1.month, day=current_date1.day)
start_period = current_date - \
    timedelta(days=current_date.weekday()) + timedelta(days=5)

for i in users:
    i["birthdate"] = i["birthdate"].replace(year=current_date.year)
    if i["birthdate"] < current_date:
        i["birthdate"] = i["birthdate"].replace(year=current_date.year + 1)


def datetime_week(wday):
    rez = current_date - \
        timedelta(days=current_date.weekday()) + timedelta(days=wday+4)
    return rez


weekday = ["Tuesday", "Wednesday", "Thursday", "Friday"]
Name = ""
# Monday
for i in users:
    if i["birthdate"] in [datetime_week(2), datetime_week(3), datetime_week(4)]:
        Name += i["name"] + ", "
if Name:
    print(f"Monday : {Name}")
    Name = ""

for x in range(4):
    for i in users:
        if i["birthdate"] == datetime_week(x+5):
            Name += i["name"] + ", "
    if Name:
        print(f"{weekday[x]} : {Name}")
        Name = ""
