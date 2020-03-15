from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from flask import flash, render_template, request, redirect
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cloud_assignment"]
mycol = mydb["books"]

app = Flask(__name__,template_folder="template")
req =" "
multikeys = []
catalogue = []
log=[]
frequency=[]

@app.route("/")
def index():
	return render_template('search_page.html')

@app.route("/search",methods=['POST','GET'])
def search():
	start=time.time()
	global req
	req= request.form.get('search')
	inc =0
	frequency.append(req)
	data = mycol.find({'author':req})
	newdata = mycol.find({'author':req})
	count= mycol.find({'author':req}).count()
	for word in frequency:
		if req in word:
			inc = inc+1
		else:
			inc =1
	print(frequency)
	print(count)
	end= time.time()- start
	logentry={'Keyword': req, "time taken" : end, "frequency": inc }
	log.append(logentry)
	with open('Logs.json', 'w', encoding='utf-8') as f:
				json.dump(log, f, ensure_ascii=False, indent=4)


	if(count>0):
		for x in newdata:
			entry={'author': req, 'title':(x["title"])}
			catalogue.append(entry)
			with open('catalogue.json', 'w', encoding='utf-8') as f:
				json.dump(catalogue, f, ensure_ascii=False, indent=4)
		return render_template('search_page.html',data=data)
	else:
		return "Unsuccessful search, Not found in Database"



@app.route("/note",methods=['POST','GET'])
def note():
	count= mycol.find({'author':req}).count()
	print(req)
	print(count)
	if(count>0):
		req_note= request.form.get('note')
		entry = {'author': req , 'Note': req_note}
		multikeys.append(entry)
		with open('Note.json', 'w', encoding='utf-8') as f:
			json.dump(multikeys, f, ensure_ascii=False, indent=4)
			f.close()
		return entry
	else:
		return "No author found for the entered name"
	

@app.route("/retrieval", methods=['POST','GET'])
def retrieval():
	with open('Note.json') as infile:
		newdata = json.load(infile)
		"""print(newdata)
								for i in newdata:
									print(i)
									if i['title'] == req:"""
		return render_template('search_page.html',newdata=newdata)
		"""else:
									return "No Note Saved for the Author"
						"""
if __name__ == '__main__':
	app.run(debug = True)