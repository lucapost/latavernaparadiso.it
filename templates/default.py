# Author:      Marco Squarcina <lavish@gmail.com>
# License:     MIT, see LICENSE for details

import datetime

author = "Luca Postregna"
path_separator = "/"
prefix = "/"
home = "/"
src_ext = {"textile": "textile"}
dst_ext = "html"
hidden = set(["404.textile", "500.textile"])
current_time = datetime.datetime.now()

def header(node):
	"""Builds the header and returns it to a string."""
	return '''<!DOCTYPE html>
	<html lang="''' + language + '''">
	<head>
		<title>''' + title + ' | ' + node.name + '''</title>
		<meta name="author" content="''' + author + '''" />
		<meta name="keywords" content="''' + keywords + '''" />
		<meta name="description" content="''' + description + '''" />
		<meta content="text/html; charset=UTF-8" http-equiv="content-type" />
		<link rel="shortcut icon" href="/images/bassanese.ico" />
		<link rel="stylesheet" type="text/css" media="all" href="/css/style.css" /> 
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
		<script type="text/javascript" src="/js/hashgrid.js"></script>  
		<script type="text/javascript" src="/js/flux.min.js"></script>  
		<script type="text/javascript" src="/js/slider.js"></script>  
		<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
		<script type="text/javascript" src="http://widgets.twimg.com/j/2/widget.js"></script>
		<script type="text/javascript" src="/js/googleanalytics.js"></script>  
	</head>
	<body>
		<header class="container_16">
			<div id="title" class="grid_10">
				<h1>''' + site_name + '''</h1>
				<h1>''' + subname + '''</h1>
				<h2>''' + site_desc + '''</h2>
			</div>
			<div id="hright" class="grid_6 clearfix">
				<div id="buttons">
					<div id="flagit">
						<a href="/" title="sito in italiano">
							<p class="hide">it</p>
						</a> 
					</div>
					<div id="twitter">
						<a href="https://twitter.com/#!/allabassanese" title="Taverna Paradiso on Twitter">
							<p class="hide">twitter</p>
						</a>
					</div>
					<div id="facebook">
						<a href="http://goo.gl/fDD4o" title="Taverna Paradiso on Facebook">
							<p class="hide">facebook</p>
						</a>
					</div>
					<div id="googleplus">
						<g:plusone count="false"></g:plusone> 
					</div>
				</div>
				<div id="contacts">
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
