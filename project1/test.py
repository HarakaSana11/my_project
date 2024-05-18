import unittest
import logging
from tests import test_module

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setUpModule():
    logger.info("Setting up module")

def tearDownModule():
    logger.info("Tearing down module")

if __name__ == "__main__":
    test_module.setUpModule = setUpModule
    test_module.tearDownModule = tearDownModule
    suite1 = unittest.TestLoader().loadTestsFromTestCase(test_module.TestFoo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(test_module.TestBar)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suite)
