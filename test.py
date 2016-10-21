#!/usr/bin/env python
# coding: utf-8
from pystache.tests.main import main as run_tests_with_junit 

import unittest
import xmlrunner

def runner(output='python_tests_xml'):
    return xmlrunner.XMLTestRunner(
        output=output
    )

def find_tests():
    return unittest.TestLoader().discover('pystache')

if __name__ == '__main__':
    runner().run(find_tests())
