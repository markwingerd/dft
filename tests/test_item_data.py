#!/usr/bin/env python
#coding:utf-8



# Tests for the fitting module
import sys, os
import unittest
import sqlite3
# My path to the project. You may need to change this
sys.path.append("/home/reimus/workspace/dft/")

from item_data import (
	ItemDatabase
)

class TestItemDatabase(unittest.TestCase):
	""" Tests the ItemDatabase class """

	def setUp(self):
		# Reloads the test database files. THIS SHOULD BE DONE FIRST.
		os.remove('./test_items.db')
		self.itemdb = ItemDatabase('test_items.db')

		self.db_cursor = sqlite3.connect('test_items.db').cursor()

	def test_initialization(self):
		""" Tests that the initialization works properly. 
			- Add a way to verify the correct data type for the columns.
		"""

		# Test that all the dropsuit columns exist
		expected_dropsuits = ['id', 'name', 'race', 'meta_level', 
				'price_isk', 'price_aur']
		self.db_cursor.execute('select * from dropsuits')
		# gets a list of only the column names
		dropsuits = map(lambda item: item[0], self.db_cursor.description)

		# Test that all the module columns exist
		expected_modules = ['id', 'name', 'meta_level', 'price_isk',
				'price_aur', 'slot_type']
		self.db_cursor.execute('select * from modules')
		modules = map(lambda item: item[0], self.db_cursor.description)

		# Test that all the module columns exist
		expected_weapons = ['id', 'name', 'meta_level', 'price_isk',
				'price_aur', 'base_damage']
		self.db_cursor.execute('select * from weapons')
		weapons = map(lambda item: item[0], self.db_cursor.description)
		print self.db_cursor.description

		self.assertItemsEqual(dropsuits, expected_dropsuits)
		self.assertItemsEqual(modules, expected_modules)
		self.assertItemsEqual(weapons, expected_weapons)


if __name__ == '__main__':
    unittest.main()