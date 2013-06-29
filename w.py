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
def open_links(answer, list_links):
	if answer == 'y' or answer == 'yes':
		for i in list_links:
			webbrowser.open(i, new=1, autoraise=False)
			print 'opened: ' + i
	else:
		print 'Done!'


def main():
	f = raw_input('Should we open up the first set of links? ')
	open_links(f, std_pages)
	c = raw_input('Would you like the secondary set of pages opened? ')
	open_links(c, sec_pages)
	e = raw_input('Would you like the work set of pages opened? ')
	open_links(e, work_pages)
	print "Thank you and have a really nice day!"





# run main when called
if __name__ == "__main__":
	main()