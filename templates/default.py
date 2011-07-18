# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

site_name = "Taverna Paradiso <br/> (alla Bassanese)"
site_desc = "Ristoratori a Cividale del Friuli"
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
		<script type="text/javascript" src="/js/jquery.jtweetsanywhere-1.2.1.min.js" ></script>
		<meta name="robots" content="index,follow" />
		<meta name="author" content="''' + author + '''" />
		<title>''' + site_name + ' - ' + node.name + '''</title>
	</head>
	<body>
		<div class="container_16">
			<header class="grid_10">
				<h1>''' + site_name + '''</h1>
				<h2>''' + site_desc + '''</h2>
			</header>
			<div id="contacts" class="grid_6 clearfix">
				di Alessio Mauro e Manuela Vogrig<br/>
				<a href="http://maps.google.it/maps/place?cid=3477028844032398125">Via Cavour 21, Cividale del Friuli - UD - Italy</a><br/><br/>

				tel/fax: +39 0432 732438<br/>
			     	email: info@tavernaparadisoXXXX.it<br/><br/>

			     	p.iva: 02629540309
			</div>
			<div class="clear"></div>
		</div>
		<div id=center>
			<div class="container_16">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
			</div>
		</div><!-- chiuso center -->
		<div class="container_16">
			<footer class="grid_16 clearfix">
				&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name">Luca Postregna</a> ::
				<a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">license</a> ::
				<a href="http://validator.w3.org/check?uri=referer">xhtml</a> <a href="http://jigsaw.w3.org/css-validator/check/referer">css</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + '''
			</footer>
			<div class="clear"></div>
		</div>
	</body>
</html>'''
