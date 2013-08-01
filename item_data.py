#!/usr/bin/env python
#coding:utf-8

import sqlite3
import exceptions


APILEVEL = '2.0'
THREADSAFETY = 0
PARAMSTYLE = 'qmark'


class ItemDatabase():

	def __init__(self, database_file='items.db'):

		self.conn = sqlite3.connect(database_file)
		self.c = self.conn.cursor()
		try:
			self.c.execute('''CREATE TABLE dropsuits
				(id int, name text, meta_level int, price_isk int, price_aur int, race text)''')
			self.c.execute('''CREATE TABLE modules
				(id int, name text, meta_level int, price_isk int, price_aur int, slot_type text)''')
			self.c.execute('''CREATE TABLE weapons
				(id int, name text, meta_level int, price_isk int, price_aur int, base_damage text)''')
		except sqlite3.OperationalError as e:
			print e

	def add_dropsuit(self, attrib_dict):
		# Get the order of the table columns
		self.c.execute('SELECT * FROM dropsuits')
		columns = map(lambda item: item[0], self.c.description)
		# Create a list of attrib_dict values in the correct order.
		item_values = []
		for key in columns:
			item_values.append(attrib_dict[key])

		self.c.execute('INSERT INTO dropsuits VALUES (?,?,?,?,?,?)', item_values)

	def add_module(self, attrib_dict):
		# Get the order of the table columns
		self.c.execute('SELECT * FROM modules')
		columns = map(lambda item: item[0], self.c.description)
		# Create a list of attrib_dict values in the correct order.
		item_values = []
		for key in columns:
			item_values.append(attrib_dict[key])

		self.c.execute('INSERT INTO modules VALUES (?,?,?,?,?,?)', item_values)

	def add_weapon(self, attrib_dict):
		# Get the order of the table columns
		self.c.execute('SELECT * FROM weapons')
		columns = map(lambda item: item[0], self.c.description)
		# Create a list of attrib_dict values in the correct order.
		item_values = []
		for key in columns:
			item_values.append(attrib_dict[key])

		self.c.execute('INSERT INTO weapons VALUES (?,?,?,?,?,?)', item_values)

	def get_dropsuit(self, value):
		self.c.execute('SELECT * FROM dropsuits WHERE id=?', (value, ))
		return self.c.fetchone()

	def get_module(self, value):
		self.c.execute('SELECT * FROM modules WHERE id=?', (value, ))
		return self.c.fetchone()

	def get_weapon(self, value):
		self.c.execute('SELECT * FROM weapons WHERE id=?', (value, ))
		return self.c.fetchone()


if __name__ == '__main__':
	itemdb = ItemDatabase()