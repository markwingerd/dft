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
				(id int, name text, race text, meta_level int, 
				price_isk int, price_aur int)''')
			self.c.execute('''CREATE TABLE modules
				(id int, name text, meta_level int, price_isk int, 
				price_aur int, slot_type text)''')
			self.c.execute('''CREATE TABLE weapons
				(id int, name text, meta_level int, price_isk int, 
				price_aur int, base_damage text)''')
		except sqlite3.OperationalError as e:
			print e

if __name__ == '__main__':
	itemdb = ItemDatabase()