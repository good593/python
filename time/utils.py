from dateutil import tz

from datetime import datetime, timedelta
from pytz import timezone

def get_yesterday(timeZone='Asia/Seoul'):
  today = datetime.now(timezone(timeZone))
  return (today - timedelta(days = 1)).strftime('%Y%m%d')

def get_today(timeZone='Asia/Seoul'):
  return datetime.now(timezone(timeZone)).strftime('%Y%m%d')

def get_targetdayTz(ptz: str, pTargetDay: str = None) -> str:
	defaul_zone = 'UTC'
	utc_zone = tz.gettz('UTC')
	target_zone = tz.gettz(ptz)
	
	if not pTargetDay:
		temp = datetime.strptime(get_yesterday(defaul_zone), '%Y-%m-%d').replace(tzinfo=utc_zone)
	else:
		temp = datetime.strptime(pTargetDay, '%Y-%m-%d').replace(tzinfo=utc_zone)
	
	return temp.astimezone(target_zone).strftime("%Y-%m-%d %H:%M:%S")

  