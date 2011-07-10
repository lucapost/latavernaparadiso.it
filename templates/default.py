# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

site_name = "Taverna Paradiso"
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
		<script type="text/javascript" src="/js/jquery.jtweetsanywhere-1.2.1.min.js"></script>  
		<meta name="robots" content="index,follow" />
		<meta name="author" content="''' + author + '''" />
		<title>''' + site_name + ' - ' + node.name + '''</title>
	</head>
	<body>
		<div class="container_16">
			<header class="grid_16 clearfix">
				<h1>''' + site_name + '''</h1>
				<h2>''' + site_desc + '''</h2>
			</header>
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
			<div class="grid_4">
				<h2>Contatti</h2>
				Taverna Paradiso <br/>
				di Alessio Mauro e Manuela Vogrig<br/>
				<a href="http://maps.google.it/maps/place?cid=3477028844032398125">Via Cavour 21, Cividale del Friuli<br/>
				Udine, Italy</a><br/><br/>

				cf: mralss72b08c758c<br/>
				p.iva: 02629540309<br/><br/>

				tel/fax: +39 0432 732438<br/>
				email: info@tavernaparadisoXXXX.it
			</div>
			<div class="grid_8">
				<h2>Appuntamenti</h2>
				<div id="jTweetsAnywhereSample"></div>
				<script>
					$('#jTweetsAnywhereSample').jTweetsAnywhere({
					username: 'lucaposttest',
					count: 3
					});
				</script>
			</div>
			<div class="grid_4 clearfix">
				<h2>Social</h2>
				<a href="http://www.facebook.com/profile.php?id=100002548877960"><div id="facebook"></div></a>
				<a href="http://twitter.com/lucaposttest"><div id="twitter"></div></a>
			</div>
			<div class="clear"></div>
		</div>
		<div class="container_16">
			<footer class="grid_16 clearfix">
				&copy; ''' + str(current_time.year) + ''' <a href="http://luca.postregna.name">Luca Postregna</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + ''' ::
				<a href="http://validator.w3.org/check?uri=referer">xhtml</a> <a href="http://jigsaw.w3.org/css-validator/check/referer">css</a>
			</footer>
			<div class="clear"></div>
		</div>
	</body>
</html>'''
