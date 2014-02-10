#!/usr/bin/env python

# POST call to QR img generator
# 
# import urllib, urllib2
# data = urllib.urlencode({'url': longUrl })
# req = urllib2.Request(appURL)
# imgr = urllib2.urlopen(req, data)
# img = imgr.read()
# self.response.headers['Content-Type'] = "image/png"
# self.response.out.write(img)

import urllib, urllib2, logging, json
from StringIO import StringIO

def img(appURL, longUrl):
	data = urllib.urlencode({'url': longUrl })
	req  = urllib2.Request(appURL)
	imgr = urllib2.urlopen(req, data)
	img  = imgr.read()
	return img

def qrUrl(longUrl, short=True , qr='', sz="250", err="L"):
	qrUrl = longUrl
	if short:
		GOOGLE_API_KEY = 'AIzaSyDSELFN2_lCmpCnxjOGbsSJWBQpZwoDBHI'
		values = json.dumps({'longUrl' : longUrl})
		requestUrl = "https://www.googleapis.com/urlshortener/v1/url?key=" + GOOGLE_API_KEY
		headers = {'Content-Type' : 'application/json'}
		req = urllib2.Request(requestUrl, values, headers)
		response = urllib2.urlopen(req)
		the_page = response.read()
		io = StringIO(the_page)
		jsonReturned = json.load(io)
		qrUrl = jsonReturned["id"]
		
	if qr:
		err = ( "L" if not (err=="L" or err=="M" or err=="Q" or err=="H") else err)
		res2 = urllib2.urlopen('http://chart.apis.google.com/chart?chs='+sz+'x'+sz+'&cht=qr&chld='+err+'|0&chl=' + urllib.quote(qrUrl))
		img = res2.read()
		return img
	else:
		return qrUrl

