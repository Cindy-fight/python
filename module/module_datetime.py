from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

print(now.timestamp())
print(dt.timestamp())

t = 1429417200.0
n = 1510120907.215664
print(datetime.fromtimestamp(t))
print(datetime.fromtimestamp(n))

print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

day = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(day)

pre = now + timedelta(hours=10)
print(pre)
after = now - timedelta(days=1)
print(after)
future = now + timedelta(days=2, hours=12, minutes=30)
print(future)

tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
value = datetime(2015,5,18,17,2,10,871012, tzinfo=timezone(timedelta(0, 28800)))
print(value)

# UTC时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 东京时间
dj_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt)
# 东京时间 北京时间转为东京时间
dj_dt1 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt1)

# practice
import re
def to_timestamp(dt_str, tz_str):
    dts = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_arr = re.match(r'^UTC([+|-]\d{1,2}):00$', tz_str)
    tz = int(tz_arr.group(1))
    dt1 = dts.replace(tzinfo=timezone(timedelta(hours=tz)))
    print(dt1)
    print(dt1.timestamp())
    print('Success')

to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')

to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')


w = datetime.now()
print(w)
print(type(w))

s = str(w)
print(s)

print(s[0:19])
