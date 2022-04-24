import boto3, json

from datetime import datetime, timedelta
from pytz import timezone

__all__ = ['get_yesterday', 'get_today', 'json_load_s3', 'json_dump_s3']

def get_yesterday(timeZone='Asia/Seoul'):
  today = datetime.now(timezone(timeZone))
  return (today - timedelta(days = 1)).strftime('%Y%m%d')

def get_today(timeZone='Asia/Seoul'):
  return datetime.now(timezone(timeZone)).strftime('%Y%m%d')
