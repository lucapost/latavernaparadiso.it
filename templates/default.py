# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

site_name = "Taverna Paradiso"
site_desc = "Ristorantori a Cividale del Friuli"
author = "Luca Postregna"
src_dir = "source"
dst_dir = "."
prefix = "/"
home = "home"
path_separator = ">"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""

	return '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script>  
		<script type="text/javascript" src="/js/jquery.jtweetsanywhere-1.2.1.min.js"></script>  
		<meta name="robots" content="index,follow" />
		<meta name="author" content="''' + author + '''" />
		<title>''' + site_name + ' - ' + node.name + '''</title>
	</head>
	<body>
		<div id="top" class="container_16">
			<header class="grid_16 clearfix">
				<div id="title">
					<h1>''' + site_name + '''</h1>
				</div>	
				<div id="subtitle">
					<p>''' + site_desc + '''</p>
				</div>
			</header>
			<div class="clear"></div>
		</div>
		<div id="center">
			<div class="container_16">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
				<div class="clear"></div>
			</div>
		</div>
		<div id="bottom" class="container_16">
			<footer>
				<div class="grid_4 alpha">
					di Alessio Mauro e Manuela Vogrig<br/>
					<a href="http://goo.gl/7wZJm">Via Cavour 21<br/>
					Cividale del Friuli, Udine, Italy<br/></a>
				</div>					
				<div class="grid_4">
					tel/fax: +39 0432 732438<br/>
					email: info@tavernaparadisoXXXX.it
				</div>
				<div class="grid_4">
					cf: mralss72b08c758c<br/>
					p.iva: 02629540309
				</div>
				<div class="grid_4 clearfix omega">
					&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name">Luca Postregna</a><br/>
					update: ''' + str(current_time.strftime("%Y%m%d")) + ''' 
				</div>
				<div class="clear"></div>
			</footer>
		</div>
	</body>
</html>'''
