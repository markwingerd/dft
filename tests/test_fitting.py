#!/usr/bin/env python
#coding:utf-8

# Tests for the fitting module
import sys
import unittest
# My path to the project. You may need to change this.
sys.path.append("/home/reimus/workspace/dft/")

from fitting import (
	Fitting
)

class TestFitting(unittest.TestCase):
	""" Tests the fitting class """

	def test_initialization(self):
		""" Tests that the initialization works properly. """
		fitting = Fitting(0,0)

		self.assertEquals(fitting.id, 0)
		self.assertEquals(fitting.dropsuit_base_id, 0)
		self.assertEquals(fitting.dropsuit_base, 'enter something here')
		self.assertEquals(fitting.total_price_isk, 0)
		self.assertEquals(fitting.total_price_aur, 0)

if __name__ == '__main__':
    unittest.main()