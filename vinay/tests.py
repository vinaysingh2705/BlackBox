from django.test import TestCase


class TestSomething(TestCase):
    
    def test_name(self):
        print("vinay")
        self.assertEqual(1,1)