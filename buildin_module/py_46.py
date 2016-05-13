#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta, timezone

# build-in: datetime
now = datetime.now()
print(now)
dt = datetime(2016, 5, 13, 12)
print(dt)

# timestamp
ts = dt.timestamp()
print(ts)
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))

# strptime & strftime
day = datetime.strptime('2016-5-13 12:11:21', '%Y-%m-%d %H:%M:%S')
print(day)
sd = day.strftime('%Y-%m-%d %H:%M:%S')
print(sd)

# calculate on datetime
print(day + timedelta(days=1, hours=2))

# change the timezone
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)
