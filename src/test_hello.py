import unittest
import xmlrunner
from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

    def test_hello_world_fails(self):
        self.assertEqual(hello_world(), "Hello, Universe!")

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
