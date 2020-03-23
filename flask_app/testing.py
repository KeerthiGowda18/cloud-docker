from app import app 
import unittest 
import os
from pymongo import MongoClient
import pymongo
import json


class TestStringMethods(unittest.TestCase): 
      
    def setUp(self):
        self.app = app.test_client() 
        app.testing = True
    
    def test_Database(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["cloud_assignment"]
        mycol = mydb["books"]     
        query1=mycol.find_one({'author':"F. Marion Crawford"})
        query2=mycol.find_one({'author':"Saurabh Dey"})
        self.assertTrue(query1)
        self.assertFalse(query2)
        
    def test_Database_Collections(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["cloud"]
        mycol = mydb["books"]     
        query1=mycol.find_one({'author':"F. Marion Crawford"})
        query2=mycol.find_one({'author':"Saurabh Dey"})
        self.assertFalse(query1)
        self.assertFalse(query2)

    def test_Database_Record_Empty(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["cloud_assignment"]
        mycol = mydb["books"]     
        query1=mycol.find_one({'author':""})
        self.assertTrue(query1)

    def test_Search_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertTrue(response.status_code, 200)

    def test_Search1(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertNotEqual(response.status_code,500)
        print(response)

    def test_search_author(self):
        with open('catalogue.json') as infile:
            newdata = json.load(infile)
            for i in newdata:
                if i['author']== "F. Marion Crawford":
                    self.assertTrue(i['author']== "F. Marion Crawford")
                    self.assertFalse(i['author']=="Saurabh Dey")

    def test_search_autho_empty(self):
         with open('catalogue.json') as infile:
            newdata = json.load(infile)
            for i in newdata:
                if i['author']=="":
                   self.assertFalse(i['author']== "")

    def test_title_search(self):
        with open('catalogue.json') as infile:
            newdata = json.load(infile)
            for i in newdata:
                if i['title']== "The Primadonna":
                    self.assertTrue(i['title']== "The Primadonna")
                    self.assertFalse(i['author']=="")

    def test_Note_Save(self):
        multikeys=[]
        with open('catalogue.json') as infile:
            newdata = json.load(infile)
            for i in newdata:
                if i['author']== "F. Marion Crawford":
                    entry= {'author': "F. Marion Crawford" , 'Note': "The Notes check for the author"}
                    multikeys.append(entry)
                    with open('NotesTest.json', 'w', encoding='utf-8') as f:
                        json.dump(multikeys, f, ensure_ascii=False, indent=4)
       
        with open('NotesTest.json') as infile:
            data = json.load(infile)          
            for i in data:
                if i['Note']== "The Notes check for the author":
                    self.assertTrue(i['Note']=="The Notes check for the author")

    def test_Note_Save_empty_author(self):
        multikeys=[]
        with open('catalogue.json') as infile:
            newdata = json.load(infile)
            for i in newdata:
                if i['author']== "":
                    entry= {'author': "" , 'Note': "The Notes check for the author"}
                    multikeys.append(entry)
                    with open('NotesTest.json', 'w', encoding='utf-8') as f:
                        json.dump(multikeys, f, ensure_ascii=False, indent=4)
       
        with open('NotesTest.json') as infile:
            data = json.load(infile)          
            for i in data:
                if i['Note']== "The Notes check for the author":
                    self.assertFalse(i['Note']=="")

if __name__ == '__main__': 
    unittest.main() 