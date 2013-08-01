#!/usr/bin/env python
#coding:utf-8

import sqlite3
import exceptions


APILEVEL = '2.0'
THREADSAFETY = 0
PARAMSTYLE = 'qmark'


class ItemDatabase():
	DROPSUIT = 'dropsuits'
	MODULE = 'modules'
	WEAPON = 'weapons'
	SEL_COLUMNS = {DROPSUIT: 'SELECT * FROM dropsuits',
				   MODULE: 'SELECT * FROM modules',
				   WEAPON: 'SELECT * FROM weapons'}
	INS_TEXT = {DROPSUIT: 'INSERT INTO dropsuits VALUES (?,?,?,?,?,?)',
			    MODULE: 'INSERT INTO modules VALUES (?,?,?,?,?,?)',
				WEAPON: 'INSERT INTO weapons VALUES (?,?,?,?,?,?)'}
	SEL_TEXT = {DROPSUIT: 'SELECT * FROM dropsuits WHERE id=?',
				MODULE: 'SELECT * FROM modules WHERE id=?',
				WEAPON: 'SELECT * FROM weapons WHERE id=?'}

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

	def add(self, table_id, attrib_dict):
		columns = self.get_columns(table_id)
		# Create a list of attrib_dict values in the correct order.
		item_values = []
		for key in columns:
			item_values.append(attrib_dict[key])

		self.c.execute(self.INS_TEXT[table_id], item_values)

	def get(self, table_id, value):
		self.c.execute(ItemDatabase.SEL_TEXT[table_id], (value, ))
		return self.c.fetchone()

	def get_columns(self, table_id):
		# Get a list of the columns in the right order
		self.c.execute(ItemDatabase.SEL_COLUMNS[table_id])
		return map(lambda item: item[0], self.c.description)


if __name__ == '__main__':
	itemdb = ItemDatabase()