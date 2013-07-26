#!/usr/bin/env python
#coding:utf-8

# Holds the fitting Class.

class Fitting():
	def __init__(self, fitting_id, dropsuit_base_id):
		self.id = fitting_id
		self.dropsuit_base_id = dropsuit_base_id
		self.dropsuit_base = 'wat?' # TACKLE THIS AFTER DB
		self.total_price_isk = 0
		self.total_price_aur = 0