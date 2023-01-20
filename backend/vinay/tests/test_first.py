from django.test import TestCase
import time


class TestSomethingElse(TestCase):
    
    def test_name(self):
        time.sleep(10)
        self.assertEqual(1,1)
    def test_name1(self):
        time.sleep(1)
        self.assertEqual(1,1)
    def test_name2(self):
        time.sleep(2)
        self.assertEqual(1,1)
