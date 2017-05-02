#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import datetime
from compiler.ast import flatten
import time
dict0={
'元旦':['20150101','20150102','20150103','20160101'],
'春节':['20150218','20150219','20150220','20150221','20150222','20150223','20150224'
'20160207','20160208','20160209','201602010','201602011','20160212','201602013'],
'清明节':['20150405','20160404'],
'劳动节':['20150501','20160501'],
'端午节':['20150620','20160609','20160610','20160611'],
'中秋节':['20150927','20160915','20160916','20160917'],
'国庆节':['20151001','20151002','20151003','20151004','20151005','20151006','20151007',
'20161001','20161002','20161003','20161004','20161005','20161006','20161007']}

def get_holidays(list_days):
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
	someday='20150622'
	days1=get_holidays(dict0)
	print get_day_type(someday,days1)