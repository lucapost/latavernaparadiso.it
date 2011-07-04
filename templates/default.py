# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

site_name = "Taverna"
site_desc = "Ristoratori a ..."
author = "Luca Postregna"
src_dir = "source"
dst_dir = "."
prefix = "/"
home = "home"
path_separator = ">"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile", "privacy.textile", "info.textile"])
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
		<meta name="robots" content="index,follow" />
		<meta name="author" content="''' + author + '''" />
		<title>''' + site_name + ' - ' + node.name + '''</title>
	</head>
	<body>
		<div id="top" class="container_12">
			<header class="grid_12 clearfix"><a href="/">
				<div id="title">
					<h1 class="hide">''' + site_name + '''</h1>
				</div>	
				<div id="subtitle">
					<p>''' + site_desc + '''</p>
				</div>
			</header>
			<div class="clear"></div>
		</div>
		<div id="center">
			<div class="container_12">
				<div id="main" class="grid_7">
'''
def footer(node):
	"""Builds the footer and returns it to a string."""
	return '''
				</div>
				<div id="images" class="grid_5 clearfix">
					images
				</div>
				<div class="clear"></div>
			</div>
		</div>
		<div id="bottom" class="container_12">
			<footer class="grid_12 clearfix">
					   footer 
			</footer>
			<div class="clear"></div>
		</div>
	</body>
</html>'''
