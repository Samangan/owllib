import unittest
from testEntities import TestEntityFunctions
from testOntology import TestOntologyFunctions

suite = unittest.TestLoader().loadTestsFromTestCase(TestEntityFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestOntologyFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)




