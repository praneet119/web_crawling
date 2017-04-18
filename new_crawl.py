def clarifaitags(link):
	from clarifai import rest
	from clarifai.rest import ClarifaiApp
	from clarifai.rest import Image as ClImage
	import pprint
	var={}
	app = ClarifaiApp("kduAK47nde3QSpZmlcakcefyD0QOhnc4oZVMLys4", "20ZOnPa-_AY_sLzcYesRyMhtLjLULRx26tLjc3QJ")

	model = app.models.get('bd367be194cf45149e75f01d59f77ba7')
	image = ClImage(url=link)
	try:
		var= model.predict([image])
					#print var['data']
				#	for key in var:
				#	print key
				#	print var[key]
				#	print ("\n")
		data=var["outputs"]
				#	for i in range(len(data)):
				#	print i
				#	print data[i]
				#	print ("\n")
					
				#model.predict_by_url(url='https://static.pexels.com/phprint ("\n")otos/46239/salmon-dish-food-meal-46239.jpeg')
		array={}
		allkeys=[]
		for i in range(len( data[0]["data"]["concepts"])):

						#print data[0]["data"]["concepts"][i]["name"]
						#print data[0]["data"]["concepts"][i]["value"]
			array.update({data[0]["data"]["concepts"][i]["name"]:data[0]["data"]["concepts"][i]["value"]})
		for key in array:
			allkeys.append(key)
		return allkeys
	except:
		stringd="no tags"
		return stringd
global_var=0
import urllib2
import re 
import codecs 
import os
from bs4 import BeautifulSoup
import json
ofile  = codecs.open("outputfile.txt", "a", encoding='utf-8', errors='replace')
for k in range(90):
	web_page="http://eattreat.in/magazine/page/"+str(k+1)
	page= urllib2.urlopen(web_page)
	soup= BeautifulSoup(page,"html.parser")
	allheadings=soup.find_all("h1",{"class":"post-title"})
	all_links=[]
	for heading in allheadings:
		link=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(heading))
		all_links.append(link[0])
	for article in all_links:
		global_var+=1
		print global_var
		print article
		if global_var !=57:
			source=article
			pages= urllib2.urlopen(source)
			soup=BeautifulSoup(pages,"html.parser")
			article_heading=soup.find_all("h1",{"class":"post-title"})
			#print len(article_heading)
			if len(article_heading)>0:
				article_heading=article_heading[0].string
				article_heading=article_heading.replace("\n","")
				article_heading=article_heading.replace("\t","")
				paras=soup.find_all("p")
				shares=soup.find_all("span",{"class":"wpusb-counter"})
				images=soup.find_all("figure",{"class":"entry-thumbnail"})
				image=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(images[0]))
				image=image[0]
				shareurl="http://graph.facebook.com/?id="+source
				jsonobjecturl=urllib2.urlopen(shareurl)
				jsonobject=jsonobjecturl.read()
				f = open('data.json','w')
				f.write(jsonobject.decode('utf-8'))
				f.close()

				with open('data.json') as data_file:
					data=json.load(data_file)
				fbshare=data["share"]["share_count"]
				#print fbshare
				#print image
				#shares=shares[0].string
				#print shares
				imagetags=clarifaitags(image)
				imagetagsstring=""
				for tags in imagetags:
					imagetagsstring+=tags+","
				parasstring=""
				print imagetags
				#print paras
				total_para=[]
				for para in paras:
					para=para.string
					#para=str(para)
					if para is not None:
						para=para.replace("\n","")
						total_para.append(para)
				try:
					print article_heading
					#print total_para
				except Exception as e:
					print("error")
				for total in total_para:
					if total is not None:
						parasstring+=total+" "
				ofile.write(article_heading+"\t"+str(fbshare)+"\t"+imagetagsstring+"\t"+image+"\t"+parasstring+"\n")