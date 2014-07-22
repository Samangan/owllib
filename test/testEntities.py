import unittest
from owllib.entities import *
from owllib.ontology import Ontology

class TestEntityFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entityWithoutOntology = Entity()
        ontology = Ontology()
        print("loading test ontology")
        ontology.load(location="http://130.88.198.11/co-ode-files/ontologies/pizza.owl")

        # Get a valid class to test against
        iceCreamClass = ontology.getEntityFromURI('http://www.co-ode.org/ontologies/pizza/pizza.owl#IceCream')
        print('Found '+ iceCreamClass.uri.__str__())
        cls.validClass = iceCreamClass
        
        # Get a valid Individual to test against
        # TODO: cannot get an individual via uri?
        #americaIndividual = ontology.getEntityFromURI('http://www.co-ode.org/ontologies/pizza/pizza.owl#America')
        #print('Found '+ americaIndividual.uri.__str__())
        #cls.validIndiv = americaIndividual
                
        # Get a valid Property to test against
        hasBase = ontology.getEntityFromURI('http://www.co-ode.org/ontologies/pizza/pizza.owl#hasBase')
        print('Found '+ hasBase.uri.__str__())
        cls.validProperty = hasBase
        
    def test_syncFromOntologyThrowsExceptionOnEntityWithNoOntology(self):
        self.assertRaises(ValueError, self.entityWithoutOntology.sync_from_ontology)

    def test_syncFromOntologyDoesNotThrowExceptionOnValidEntity(self):
        try: 
            self.validClass.sync_from_ontology()
        except ValueError:
            self.fail("There should be an associated ontology for the valid Entity")

    def test_classGet_parents(self): 
        parents = self.validClass._get_parents()
        self.assertFalse(parents is None)

    def test_classGet_children(self):
        children = self.validClass._get_children()
        self.assertFalse(children is None)

    def test_class_is_namedReturnsTrue(self):
        self.assertTrue(self.validClass.is_named())
        
    def test_PropertyGet_parents(self): 
        parents = self.validProperty._get_parents()
        self.assertFalse(parents is None)

    def test_PropertyGet_children(self):
        children = self.validProperty._get_children()
        self.assertFalse(children is None)

    def test_property_is_namedReturnsTrue(self):
        self.assertTrue(self.validProperty.is_named())
    
