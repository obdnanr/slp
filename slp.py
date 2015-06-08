#!/usr/bin/python
#
# An example from Sean Reifschneider's Python Tutorial at Linux Expo 98.
#
# Copyright (c) 1998 Sean Reifschneider, tummy.com, ltd.
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# You can contact Sean Reifschneider at
#          P.O. Box 270624,
#          Fort Collins, CO USA 80527-0624,
# or at jafo-gpl@tummy.com
#
#  Simple phone-number database module

import shelve, string

UNKNOWN = 0
HOME = 1
WORK = 2
FAX = 3
CELL = 4

class phoneentry:
    def __init__(self, name = 'Unknown', number = 'Unknown', type = UNKNOWN):
		self.name = name
		self.number = number
		self.type = type
    #  create string representation
    def __repr__(self):
		return('%s:%d' % ( self.name, self.type ))
    #  fuzzy compare or two items
    def __cmp__(self, that):
		this = string.lower(str(self))
		that = string.lower(that)
		if string.find(this, that) >= 0:
			    return(0)
		return(cmp(this, that))

    def showtype(self):
		if self.type == UNKNOWN: return('Unknown')
		if self.type == HOME: return('Home')
		if self.type == WORK: return('Work')
		if self.type == FAX: return('Fax')
		if self.type == CELL: return('Cellular')

class phonedb:
    def __init__(self, dbname = 'phonedata'):
		self.dbname = dbname;
		self.shelve = shelve.open(self.dbname);
    def __del__(self):
		self.shelve.close()
		self.shelve = None
    def add(self, name, number, type = HOME):
		e = phoneentry(name, number, type)
		self.shelve[str(e)] = e
    def lookup(self, string):
		list = []
		for key in self.shelve.keys():
			    e = self.shelve[key]
			    if cmp(e, string) == 0:
					list.append(e)
		return(list)

#  if not being loaded as a module, run a small test
if __name__ == '__main__':
    foo = phonedb()
    foo.add('Sean Reifschneider', '970-555-1111', HOME)
    foo.add('Sean Reifschneider', '970-555-2222', CELL)
    foo.add('Evelyn Mitchell', '970-555-1111', HOME)
    print 'First lookup:'
    for entry in foo.lookup('reifsch'):
		print '%-40s %s (%s)' % ( entry.name, entry.number, entry.showtype() )
    print
    print 'Second lookup:'
    for entry in foo.lookup('e'):
		print '%-40s %s (%s)' % ( entry.name, entry.number, entry.showtype() )
