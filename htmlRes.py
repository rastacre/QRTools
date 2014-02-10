#!/usr/bin/env python
import urllib


def htmlQR(opt):
	
	title = ( opt.get('title') if 'title' in opt.keys() else "QRTools")
	debug = ( "<div id='dbug'></div>" if 'debug' in opt.keys() and opt.get('debug') == True else "" )
	domain = (opt.get('domain') if 'domain' in opt.keys() else "[QRTools]" )
	longUrl = (opt.get('longUrl') if 'longUrl' in opt.keys() else "" )
	shortUrl = (opt.get('shortUrl') if 'shortUrl' in opt.keys() else "" )
	
	html = """
<html>
	<head>
		<title>""" + title + """</title>
		<link rel="SHORTCUT ICON" href="/img/favicon.ico" />
		<link rel="stylesheet" type="text/css" href="/stylesheets/style.css" />
		<link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.10.3/themes/ui-lightness/jquery-ui.css" />
		<script type="text/javascript" src="/scripts/qrtools.js"></script>
		<script type="text/javascript" src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
		<script type="text/javascript" src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
	</head>
	<body>
		""" + debug + """
		<div class="wrapper">
			<div id="qrForm">
				<button id='qrType'>URL</button>
				<button id='qrTypeSelect'>Select text Type</button>
				<input class='textinput ui-corner-all ui-widget ui-widget-content ui-state-default' type='text' name='url' id='qrInput' placeholder='Type the URL to shorten and to convert in QR'/>
				<button id='qrSubmit'>Submit</button>
				<button id='showhelp'>Help</button>
			</div>
			<ul id="qrTypeSelectList">
				<li><a href="#" name="url" placeholder="Type the URL to shorten and to convert in QR">URL</a></li>
				<li><a href="#" name="text" placeholder="Type the Text to convert in QR">Text</a></li>
				<li><a href="#" name="phone" placeholder="Type the Phone Number to convert in QR">Phone #</a></li>
			</ul>
			""" + help( domain ) + """
			<div id='result'>"""+("""
				<div class='result ui-corner-all ui-widget ui-widget-content'>
					<div class="img_div qr">
						<a target="blank" href='""" + shortUrl + """'><img class='qrresult ui-corner-left' alt='""" + shortUrl + """' title='""" + shortUrl + """' src='""" + domain + """/qr?url=""" + urllib.quote_plus(longUrl) + """' /></a>
					</div>
					<div class="links_div">
						<p><b>URL:</b><br/><a class='lurl' target="blank" href='""" + longUrl + """'>""" + longUrl + """</a></p>
						"""+("""<p><b>Short URL:</b><br/><a target="blank" href='""" + shortUrl + """'>""" + shortUrl + """</a></p>""" if shortUrl != "" else "")+"""
						<p><b>Image Permalink:</b><br/><a target="blank" href='""" + domain + """/qr?url=""" + urllib.quote_plus(longUrl) + """'>""" + domain + """/qr?url=""" + urllib.quote_plus(longUrl) + """</a></p>
					</div>
				</div>""" if longUrl!='' else "") + """
			</div>
		</div>
		<script>init()</script>
	</body>
</html>"""
	return html


def links( longUrl, shortUrl, typeUrl, domain):
	return """
		<div class='result ui-corner-all ui-widget ui-widget-content'>
			<div class="img_div qr">
				""" + ("""<a target="blank" href='""" + shortUrl + """'>""" if shortUrl!="" else "") + """<img class='qrresult ui-corner-left' alt='""" + shortUrl + """' title='""" + shortUrl + """' src='""" + domain + """/qr?"""+typeUrl+"""=""" + urllib.quote_plus(longUrl) + """' />""" + ("""</a>""" if shortUrl!="" else "") + """
			</div>
			<div class="links_div">
				<p><b>""" + ("URL" if typeUrl=='url' else typeUrl.title()) + """:</b><br/><a class='lurl' target="blank" href='""" + longUrl + """'>""" + longUrl + """</a></p>
				"""+("""<p><b>Short URL:</b><br/><a target="blank" href='""" + shortUrl + """'>""" + shortUrl + """</a></p>""" if shortUrl != "" else "")+"""
				<p><b>Image Permalink:</b><br/><a target="blank" href='""" + domain + """/qr?"""+typeUrl+"""=""" + urllib.quote_plus(longUrl) + """'>""" + domain + """/qr?"""+typeUrl+"""=""" + urllib.quote_plus(longUrl) + """</a></p>
			</div>
		</div>
		"""

def help(domain):
	att = "<p class='helpattention'>Remember to URLEncode the URL you want to convert.</p>"
	return """
			<div id='hidden' class="helpcontainer ui-widget-content ui-corner-bottom">
				<div class="helpsection">
					<h2>What is QRTools:</h2>
					<p><b>QRTools</b> generate QR codes from a URL which is first shorten using <b><a href="http://goo.gl" target="_blank">goo.gl</a></b> API.</p>
					<p><b>QRTools</b> can also be used to generate QR codes only (as PNG mime type) for shortened and unshortened URLs.</p>
					<p>In attition <b>QRTools</b> can be used as a bookmarklet to generate QR codes on the fly for the pages you are reading.</p>
				</div>
				<div class="helpsection">
					<h2>Usage:</h2>
					<ul>
						<li><a href='#urls'>QRTools as a URL shortener</a></li>
						<li><a href='#png'>QRTools as a QR PNG generator</a></li>
						<li><a href='#bm'>QRTools as a Bookmarklet</a></li>
						<li><a href='#qrerr'>Appendix</a></li>
					</ul>
					<h3 id='urls'>QRTools as a URL shortener:</h3>
					<div class="innerhelpsection">
						<p>You can submit a URL at <a href='""" + domain + """'>""" + domain + """</a> to generate a shortened URL and a QR code for it.</p>
						<p>You can also use a direct URL to QRTools in order to generate the shortened URL and QR, in the form of:</p>
						<pre>""" + domain + """?url=[URL]</pre>
						""" + att + """
						<p>This function supports both GET and POST requests.</p>
					</div>
					<h3 id='png'>QRTools as a QR PNG generator:</h3>
					<div class="innerhelpsection">
						<p>QRTools can generate PNG images of a URL's QR that can be used as img src using a direct URL.</p>
						<p>With this method it is possible to generate QR codes for both shortened and unshortened URLS:</p>
						<p>For shortened URL use:</p>
						<pre>""" + domain + """/qr?[url=[URL]</pre>
						""" + att + """
						<p>For unshortened URL, Text or Phone Numbers use:</p>
						<pre>""" + domain + """/qrl?[url|text|phone]=[URL|String|Phone #]</pre>
						""" + att + """
						<p>By default QRTools will generate a 250px X 250px image of a QR with <a href="#qrerr">Low error recovery</a>.</p>
						<p>Text and Phone # QRs cannot be shortened.</p>
						<p>These properties can be modified (for bot qr/ and qrl/ calls), by adding the following parameters to the image call:</p>
<pre>
sz=[image width]

err=[error level]
</pre>
						<p>Like so:</p>
<pre>
""" + domain + """/qr?url=[URL]&sz=500&err=H

""" + domain + """/qrl?[url|text|phone]=[URL|String|Phone #]&sz=500&err=H
</pre>
					<p>These image calls will generate QR with of 500px X 500px with a High level of error recovery.</p>
					<p>For example: the URL http://www.google.com would generate the following QR image:</p>
					<p class='helpexample'><img  class='qr' alt='""" + domain + """/qrl?url=http://www.google.com&sz=100' title='""" + domain + """/qrl?url=http://www.google.com&sz=100' src='""" + domain + """/qrl?url=""" + urllib.quote_plus('http://www.google.com') + """&sz=100' /></p>
					<p>using the following HTML tag:</p>
<pre>
&lt;img src='""" + domain + """/qrl?[url|text|phone]=[URL|String|Phone #]&sz=100&err=[L|M|Q|H]' /&gt;

where: url=[URL]        = http://www.google.com => """ + urllib.quote_plus('http://www.google.com') + """
       text=[String]    = This is a string! => """ + urllib.quote_plus('This is a string!') + """
       phone=[Phone #]  = 01-234-5678 or 01 234 5678 or 012345678
       
       sz=[image width] = 100 => 100px X 100px image
       err=[L|M|Q|H]    = L => Low error recovery
</pre>
					<p>Please note that the 'sz' and 'err' parameters are optional and do not need to be specified.</p> 
					<p>This function supports both GET and POST requests.</p>
					</div>
					
					<h3 id='bm'>QRTools as a Bookmarklet for URLs:</h3>
					<div class="innerhelpsection">
						<p>You can add QRTools to your browser's bookmarks tool bar as a bookmarklet in order to generate QR codes for the pages you are reading.</p>
						<p>At present the bookmarklet only generates a 250px X 250px image of a QR with <a href="#qrerr">Low error recovery</a>. Also the URL is shortened by default (for easier reading on mobile devices).</p>
						<p>To add the bookmarklet to you browser's bookmarks tool bar simply drag and drop the following button on the toolbar:</p>
						<p class='bookmarklet'><a href='javascript:void((function(){j=document.createElement(%22SCRIPT%22);j.src=%22http://qrtools.appspot.com/scripts/QRgen.js%22;document.getElementsByTagName(%22HEAD%22)[0].appendChild(j);})())'>Generate QR</a></br><span>Click the button to test the Bookmarklet.</span></p>
						
						<p>Or create a new bookmark using the following code as URL or Location:</p>
						<pre>javascript:void((function(){j=document.createElement(%22SCRIPT%22); j.src=%22http://qrtools.appspot.com/scripts/QRgen.js%22; document.getElementsByTagName(%22HEAD%22)[0].appendChild(j); })())</pre>
						<p>To use the bookmarklet simply open a webpage and once it finishes loading click on the bookmarklet. The generated code will appear on the top right corner.</p>
					</div>
					
					
					<h4 id='qrerr'>Appendix: QR codes Error Recovery</h4>
					<div class="innerhelpsection">
						<table>
							<tbody>
								<tr>
									<th>Error correction capacity</th>
								</tr>
								<tr>
									<td>Level L</td>
									<td>7% of codewords can be restored.</td>
								</tr>
								<tr>
									<td>Level M</td>
									<td>15% of codewords can be restored.</td>
								</tr>
								<tr>
									<td>Level Q</td>
									<td>25% of codewords can be restored.</td>
								</tr>
								<tr>
									<td>Level H</td>
									<td>30% of codewords can be restored.</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
			"""


def jsWidget(domain):
	import random
	rnd = str(random.randint(1000000000, 9999999999))
	
	return """
	if (!jQuery) {  
		alert('no Jquery - loading...')
		var script  = document.createElement('script');
		script.src  = 'http://jqueryjs.googlecode.com/files/jquery-1.3.2.js';
		script.type = 'text/javascript';
		script.defer = true;
		document.getElementsByTagName('head').item(0).appendChild(script);
	}
	
	formhtml = 	"<style>" +
				".label_""" + rnd + """{} .textinput_""" + rnd + """{} .button_""" + rnd + """ #qrt_ww_""" + rnd + """{} #qrt_ww_""" + rnd + """{}" +
				"</style>" +
				"<input class='label_""" + rnd + """' type='button' value='URL:'/>" +
				"<input class='textinput_""" + rnd + """' type='text' name='url' placeholder='Type the URL to shorten and to convert in QR'/>" + 
				"<input class='button_""" + rnd + """' type='button' value='Submit'/>"
	
	wdiv = '<div id="qrt_ww_""" + rnd + """">""" + rnd + """</br>' + formhtml + '</div>';
	
	$("#qrtools_widget").after(wdiv);
	"""
