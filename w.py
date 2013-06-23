#!/usr/bin/python

import webbrowser
# standard pages
tab1 = 'http://my.franklin.edu'
tab2 = 'http://mail.stone.tc'
tab3 = 'http://google.com/a/voxy.com'
tab4 = 'http://outlook.com'
tab5 = 'http://facebook.com'
# second pages
tab8 = 'http://www.woot.com'
# work pages
tab10 = 'http://govoxy.atlassian.net'
tab11 = 'http://www.bitbucket.org'

std_pages = [tab1, tab2, tab3, tab4, tab5]
sec_pages = [tab8]
work_pages = [tab10, tab11]

# function standard links
def open_links(answer):
	if answer == 'y' or answer == 'yes':
		for i in std_pages:
			webbrowser.open(i, new=1, autoraise=False)
			print 'opened: ' + i
	else:
		print 'Done!'

# function for second set of links
def open_second(answer):
	if answer == 'y' or answer == 'yes':
		for a in sec_pages:
			webbrowser.open(a, new=1, autoraise=False)
			print 'opened: ' + a
	else:
		print 'Done!'

# function for work links
def open_work(answer):
	if answer == 'y' or answer == 'yes':
		for d in work_pages:
			webbrowser.open(d, new=1, autoraise=False)
			print 'opened: ' + d
	else:
		print 'Done!'


def main():
	f = raw_input('Should we open up the first set of links? ')
	open_links(f)
	c = raw_input('Would you like the secondary set of pages opened? ')
	open_second(c)
	e = raw_input('Would you like the work set of pages opened? ')
	open_work(e)
	print "Thank you and have a really nice day!"




	




# run main when called
if __name__ == "__main__":
	main()