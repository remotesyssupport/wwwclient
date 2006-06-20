#!/usr/bin/env python
# Encoding: iso-8859-1
# vim: tw=80 ts=4 sw=4 noet
from os.path import join, basename, dirname, abspath
import sys ; sys.path.append(join(dirname(dirname(abspath(__file__))), "Sources"))

from wwwclient import browse, scrape

scraper = scrape.Scraper()
session = browse.Session()
session.verbose = True
session.get("www.google.com/")

search_form = scraper.forms(session.last().data()).values()[0]
session.submit( search_form, values={"q":"Britney Spears"}, action="btnG",
method=browse.GET ).data()
scrape.HTML.textOnly(session.last().data())

# EOF