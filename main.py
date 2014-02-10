#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import urllib, urllib2, httplib, htmlRes, gsAPI, webapp2, logging
#import simplejson as json
#from StringIO import StringIO
urllib.getproxies_macosx_sysconf = lambda: {}
_DEBUG = False

class QRMain(webapp2.RequestHandler):
	def get(self):
		seq = (1 if self.request.get('url') else ( 2 if self.request.get('text') else ( 3 if self.request.get('phone') else 0)))
		opt = {
			'debug' : _DEBUG,
			'domain' : self.request.host_url,
		}
		
		if seq==1:
			URL = str(self.request.get('url'))
			qrUrl = gsAPI.qrUrl(URL)
			opt.update({
				'title' :"QRTools - URL",
				'shortUrl' : qrUrl,
				'longUrl' : URL,
			})
		elif seq==2: #text request
			text = str(self.request.get('text'))
			qrURL = gsAPI.qrUrl(text, False)
			opt.update({
				'title' :"QRTools - String",
				'longUrl' : qrUrl,
			})
		elif seq==3: #phone request
			text = str(self.request.get('phone'))
			qrURL = gsAPI.qrUrl(text, False)
			opt.update({
				'title' :"QRTools - Phone Number",
				'longUrl' : qrUrl,
			})
		else:
			opt.update({'title':'QRTools'})
			
		self.response.out.write(htmlRes.htmlQR(opt))

class QRImgLong(webapp2.RequestHandler):
	def get(self):
		seq = (1 if self.request.get('url') else ( 2 if self.request.get('text') else ( 3 if self.request.get('phone') else 0)))
		sz = (str(self.request.get('sz')) if self.request.get('sz') else "250")
		err = (str(self.request.get('err')).upper() if self.request.get('err') else "L")
		
		if seq==0:
			self.error(400)
		elif seq==1:
			typeUrl = 'url'
			longUrl = str(self.request.get('url'))
			img = gsAPI.qrUrl(longUrl,False, 'qr', sz, err)
		elif seq==2:
			typeUrl = 'text'
			longUrl = str(self.request.get('text'))
			img = gsAPI.qrUrl(longUrl,False, 'qr', sz, err)
		elif seq==3:
			typeUrl = 'phone'
			longUrl = str(self.request.get('phone'))
			img = gsAPI.qrUrl("tel:"+longUrl,False, 'qr', sz, err)
		
		self.response.headers['Content-Type'] = "image/png"
		self.response.out.write(img)

class QRImg(webapp2.RequestHandler):
	def get(self):
		seq = (1 if self.request.get('url') else ( 2 if self.request.get('text') else ( 3 if self.request.get('phone') else 0)))
		sz = (str(self.request.get('sz')) if self.request.get('sz') else "250")
		err = (str(self.request.get('err')).upper() if self.request.get('err') else "L")
		
		if seq==0:
			self.error(400)
		elif seq==1:
			typeUrl = 'url'
			longUrl = str(self.request.get('url'))
			img = gsAPI.qrUrl(longUrl,True, 'qr', sz, err)
		elif seq==2:
			typeUrl = 'text'
			longUrl = str(self.request.get('text'))
			img = gsAPI.qrUrl(longUrl,False, 'qr', sz, err)
		elif seq==3:
			typeUrl = 'phone'
			longUrl = str(self.request.get('phone'))
			img = gsAPI.qrUrl("tel:"+longUrl,False, 'qr', sz, err)
		
		self.response.headers['Content-Type'] = "image/png"
		self.response.out.write(img)

class QRAjax(webapp2.RequestHandler):
	def get(self):
		seq = (1 if self.request.get('url') else ( 2 if self.request.get('text') else ( 3 if self.request.get('phone') else 0)))
		if seq==1:
			typeUrl = 'url'
			longUrl = str(self.request.get('url'))
			qrUrl = gsAPI.qrUrl(longUrl)
			self.response.out.write(htmlRes.links(longUrl, qrUrl, typeUrl, self.request.host_url))
		elif seq==2:
			typeUrl = 'text'
			longUrl = str(self.request.get('text'))
			qrUrl = gsAPI.qrUrl(longUrl, False)
			self.response.out.write(htmlRes.links(qrUrl, "", typeUrl, self.request.host_url))
		elif seq==3:
			typeUrl = 'phone'
			longUrl = str(self.request.get('phone'))
			logging.info("******###******" +longUrl +"******###******")
			qrUrl = gsAPI.qrUrl(longUrl, False)
			self.response.out.write(htmlRes.links(qrUrl, "", typeUrl, self.request.host_url))
		else:
			self.error(400)


class Widgetj(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(htmlRes.jsWidget(self.request.host_url))

app = webapp2.WSGIApplication([('/', QRMain), ('/qr', QRImg), ('/qrl', QRImgLong), ('/qwj', Widgetj), ('/qra', QRAjax)])

