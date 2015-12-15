# Hint:  use Google to find python function

from datetime import datetime

def compute_time(date_start,date_stop,date_fmt):
	a = datetime.strptime(date_start,date_fmt)
	b = datetime.strptime(date_stop,date_fmt)
	return abs((b - a).days)


####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

compute_time(date_start,date_stop,'%m-%d-%Y') # yields: 513


####b)  
date_start = '12312013'  
date_stop = '05282015'  

compute_time(date_start,date_stop,'%m%d%Y') # yields: 937


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

compute_time(date_start,date_stop,'%d-%b-%Y') # yields: 7850
