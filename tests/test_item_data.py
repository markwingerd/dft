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

		self.assertItemsEqual(dropsuits, expected_dropsuits)
		self.assertItemsEqual(modules, expected_modules)
		self.assertItemsEqual(weapons, expected_weapons)

	def test_add_item(self):
		""" Tests that items can be added to tables. """
		dropsuit_db_data = {'id': 0, 'name': 'God Suit', 'race': 'Jove', 
				'meta_level': 42, 'price_isk': 60000, 'price_aur': 600}
		module_db_data = {'id': 0, 'name': 'Duct Tape', 'meta_level': 42,
				 'price_isk': 5500, 'price_aur': 60, 'slot_type': 'Hi Slot'}
		weapon_db_data = {'id': 0, 'name': 'Ban Hammer', 'meta_level': 42,
				 'price_isk': 36, 'price_aur': 6, 'base_damage': 9999}

		self.itemdb.add(itemdb.DB_DROPSUIT, dropsuit_db_data)
		self.itemdb.add(itemdb.DB_MODULE, module_db_data)
		self.itemdb.add(itemdb.DB_WEAPON, weapon_db_data)

		expected_dropsuit_values = dropsuit_db_data.values()
		self.db_cursor.execute('SELECT * FROM dropsuits WHERE id=?', (0,))
		dropsuit_values = self.db_cursor.fetchone()

		expected_module_values = module_db_data.values()
		self.db_cursor.execute('SELECT * FROM modules WHERE id=?', (0,))
		module_values = self.db_cursor.fetchone()

		expected_weapon_values = weapon_db_data.values()
		self.db_cursor.execute('SELECT * FROM weapons WHERE id=?', (0,))
		weapon_values = self.db_cursor.fetchone()

		self.assertItemsEqual(dropsuit_values, expected_dropsuit_values)
		self.assertItemsEqual(module_values, expected_module_values)
		self.assertItemsEqual(weapon_values, expected_weapon_values)


if __name__ == '__main__':
    unittest.main()