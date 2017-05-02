#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import datetime
from compiler.ast import flatten
import time

def read_holidays(holidays_file='.\holidays.txt'):
	try:
		holidays_file=open(holidays_file,'r')
	except IOError,err:
		print 'open failed'
		return []
	days_of_holidays=[]
	holidays_dict={}
	lines=holidays_file.readlines()
	for line in lines:		
		holiday_type,dates=line.split(':')
		list_of_day=dates.split(';')
		holidays_dict[holiday_type]=list_of_day
	return holidays_dict

def get_holidays(dict0):
	days=[]
	for day in dict0.values():
		days.append(day)
	days=flatten(days)
	return days

def get_day_type(query,days):
	if query in days:
		return 1
	days_of_work=['20150104','20150622','20151010','20160206','20160214','20160612','20160918','20161008','20161009']
	if query in days_of_work:
		return 0
	a=time.strptime(query,'%Y%m%d');
	if a.tm_wday==6 or a.tm_wday==7:
		return 1
	else:
		return 0

if __name__ == '__main__':
	someday='20150621'
	holidays_dict1=read_holidays()
	days1=get_holidays(holidays_dict1)
	print get_day_type(someday,days1)
