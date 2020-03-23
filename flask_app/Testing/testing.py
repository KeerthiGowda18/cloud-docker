from app import app 
import unittest 
from pymongo import MongoClient
import pymongo


class TestStringMethods(unittest.TestCase): 
    print("inside")
    def setUp(self):
        #self.app = app.test_client() 
        #app.testing = True
    
    def test_Database(self):
        ##mydb = myclient["cloud_assignment"]
        #mycol = mydb["books"]    
        print("inside test_Database")   
        #self.assertIsNotNone(myclient)

    
  