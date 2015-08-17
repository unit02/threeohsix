#!/usr/bin/env python

# Testing Outline - unittests
PKG = 'robotsim'

import sys
import unittest

import math_test


# Basic test class showing different cases
class test_math(unittest.TestCase):    # Your test class name in form test_name

    def test_haha(self):
        self.assertTrue(math_test.math_haha() == True)


if __name__ == '__main__':
    unittest.main()
	#import rostest
	#rostest.rosrun(package_name, test_name[your choice],class name,sysargs=None[optional-overrides sys.argv])
	#rostest.rosrun( PKG, 'test_math_haha', test_lol_fail,sysargs=None)
