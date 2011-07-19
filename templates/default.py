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
		<meta name="author" content="''' + author + '''" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script>  
		<script type="text/javascript" src="/js/jquery.jtweetsanywhere-1.2.1.min.js" ></script>
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
		<script type="text/javascript">
			var _gaq = _gaq || [];
			_gaq.push(['_setAccount', 'UA-6164762-9']);
			_gaq.push(['_trackPageview']);
			(function() {
				var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
				ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
				var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			})();
		</script>
		<title>Taverna Paradiso (alla Bassanese) -''' + node.name + '''</title>
	</head>
	<body>
		<header class="container_16">
			<div id="title" class="grid_10">
				<h1>''' + site_name + '''</h1>
				<h2>''' + site_desc + '''</h2>
			</div>
			<div id="hright" class="grid_6 clearfix">
				<div>
					<g:plusone></g:plusone>
					<a href="/it" title="traduzione italiana"><img src="/images/it.jpg" title="it flag" alt="bandiera italiana" /></a><!--<a href="/de" title="deutcsh"><img alt="flag de" src="/images/de.jpg" title="de flag" /></a>-->
				</div>
				<div>
					di Alessio Mauro e Manuela Vogrig<br/>
					<a title="la Taverna Paradiso (alla Bassanese) di Cividale del Friuli su google maps" href="http://maps.google.it/maps/place?cid=3477028844032398125">Via Cavour 21, Cividale del Friuli - UD - Italy</a><br/><br/>
					tel/fax: +39 0432 732438<br/>
				     	mail: info@latavernaparadiso.it<br/><br/>
				     	p.iva: 02629540309
				</div>
			</div>
			<div class="clear"></div>
		</header>
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
				&copy; ''' + str(current_time.year) + ''' <a title="Il blog di Luca Postregna" href="http://luca.postregna.name">Luca Postregna</a> ::
				<a title="La licenza Creative Commons" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">license</a> ::
				<a title="xhtml validator" href="http://validator.w3.org/check?uri=referer">xhtml</a> <a title="css validator" href="http://jigsaw.w3.org/css-validator/check/referer">css</a> ::
				update: ''' + str(current_time.strftime("%Y%m%d")) + '''
			</footer>
			<div class="clear"></div>
		</div>
	</body>
</html>'''
