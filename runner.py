#encoding:utf-8
import unittest
import interface

mysuit = unittest.TestSuite()
mysuit.addTest(interface.MyTestCase('test_denglu'))
myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuit)