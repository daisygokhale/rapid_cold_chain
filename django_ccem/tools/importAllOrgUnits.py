import requests,json,code,csv
"""
creates three csv and json files for
 - dataSets
 - dataElements
 - indicators
 
 In the json file each elment has a _data attribute which is the json representation of that object 
"""



url = "http://212.71.248.145:8080/ccei_laos/api/"

ses = requests.Session()
ses.auth = ('admin','district')
ses.headers.update({'Accept':'application/json'})

req = []
req.append(ses.get(url+'organisationUnits/?paging=false'))

jdata = [r.json() for r in req]

data = {}
chead = ('id','code','name','shortName')
for j in jdata:
	#only one element in json data
	k = j.keys()[0]
	arr = j[k]
	data[k] = arr

	#make csv writer
	cfp = open(k+'.csv','w')
	cw = csv.writer(cfp)
	cw.writerow(chead)

	for i,obj in enumerate(arr):
		#get actual data for object using api

		r = ses.get(obj['href']+'.json')
		rd = r.json()

		if k == 'dataSets':
			obj['_data'] = {a:rd[a] for a in rd.keys() if a not in ['dataEntryForm','legendSet','organisationUnits']}
		else:
			obj['_data'] = rd

		#print i,obj['href']
		name_lang=obj['name'].split('|')
		if len(name_lang)>0:

			if(name_lang[0][0:1]>=0):# and name_lang[0][0:1]<=9):
				#print name_lang[0][0:1]
				if len(name_lang[0].split(' ',1))>1:
					name_lang[0]=name_lang[0].split(' ',1)[1]
			#print obj['id'],obj['name'],name_lang[0],name_lang[1]
		#print obj['id'],obj['name']
		crow = [obj[a] if a in obj else None for a in chead if a != 'shortName']
		crow.append(rd['shortName'])
		#cw.writerow(crow)
	cfp.close()

#write json
for k,v in data.iteritems():
	jfp = open('raw_'+k+'.json','w')
	json.dump(v,jfp,indent=4)
	jfp.close()
