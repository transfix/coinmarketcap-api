#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
from lxml.html import parse

expected_result = ['#', 'Name', 'Symbol', 'Market Cap', 'Price', 'Available Supply', 'Volume (24h)', '% 1h', '% 24h', '% 7d']

def check_table():
	page = parse("http://coinmarketcap.com/all.html")
	data = page.xpath('//tr/th//text()')
	result = ((expected_result > data) - (expected_result < data))
	return result

class coinmarketcaptestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_check_table(self):
		check_table()
		assert check_table() is 0

if __name__ == '__main__':
    unittest.main()
