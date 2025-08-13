# test_project.py
import unittest
from src.project import project as p

class TestProject(unittest.TestCase):

    def testAddContracts(self):
        self.project.addContract(contract = self.Contract(name = "name", enail="email"))
        self.assertTrue(self.project.contacts.contains("testContact"))


    # Step 4

        # Create an organization
    def setUp(self):
        self.project = p(name = "name", organisation = "organisation", contacts = ["contact1", "contact2"])

    def initialiseProjectWithAllAttributes(self):
        self.assertTrue(hasattr(self.project, "name" and "organisation" and "contacts"))

        # Create a project associated with the organisation

        # # Check if project is associated with the correct organisation


    # Step 5
    # Add a test that test a contact can be created and
    # added to an organisation and can also be added to a project


    # Challenge test that you can add a contact to an organisation
    # and a project using the project class

    def tearDown(self):
        self.project.destroy()
