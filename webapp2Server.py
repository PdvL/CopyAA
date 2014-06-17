"""A simple webapp2 server."""

import webapp2

form = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		
		<title>Daily arbitrage sports analysis</title>
		<link href="http// .css" rel="stylesheet" type="text/css">

<!--section to be deleted after finished user diagram--> 
		<style type="text/css">			
			body{
				display: block;
				width: 1000px;
				height: 0px;
				margin: 1px 172.500px;
				border-width: 0px;
				border-width: 0px;
				border-color: ;
				border-style: solid;
				padding: 5px;
				background: #000;
				font-family: verdana, helvetica, sans-serif;
				}
			
			a{
				text-decoration: none;
				text-align: center;
				color: #000;
				margin: 1px;
				border: 0px;
				padding: 1px;
				}
				a:hover{
					text-decoration:;
					color: #fff;
					background: #273b64;
					}		
						
			#chapeaux{
				margin: 0px;
				border-width: 0px;
				border-color: #000001;
				border-style: solid;
				padding: 5px;
				background: #b20500;
				color: ;
				}
				
				#chapeaux section{					
					margin: 0px;
					border-width: 1px;
					border-color: ;
					border-style: ;
					padding: 2px;
					float: right;
					height: 30px;
					}
					
				#chapeaux ul{
					list-style-type: none;
					margin: 0;
					padding: 0;
					float: right;
					}
					#chapeaux li{
						float:left;
						}
					#chapeaux a{
						display: block;
						width: 70px;						
						color: #000;
						}
					#chapeaux a:hover{
						font-weight: bold;
						text-decoration: underline;
						color: #000;
						background: #fff;
						}
					
			header{
				margin: 0px;
				border-width: 2px;
				border-color: #000001;
				border-style: solid;
				padding: 2px;
				font-family: Verdana, Helvetica, sans-serif;
				background: #fff;
				}
				
				header nav{
					margin: 0px;
					border-width: 1px;
					border-color: #000001;
					border-style: solid;
					padding-left: 2px;
					padding-right: 2px;
					padding-top: 2px;
					padding-bottom: 25px;
					}
					header nav ul{
						list-style-type: none;
						margin: 1px;
						border: 0;
						padding: 1px;
						}
					header nav li{
						float: left;
						margin: 1px;
						border: 0;
						padding: 1px;
						}
					header nav a{
						display: block;
						width: 60px;
						font-weight: bold;
						color: ;
						background: ;
						}
					header nav a.longer{
						display: block;
						width: 100px;
						}	
			#Main{
				font-family: verdana, sans-serif;
				margin: 0px;
				border-width: 0px;
				border-color: #000001;
				border-style: solid;
				padding: 0px;
				background: #b20500;
				width: ;
				height: 1400px;
				}
				
				#Main h1{
					h1-style-type: none;
					margin: 2px;
					border: 0;
					padding: 0;
					}
				
				#slider{
					margin: 0px;
					border-width: 2px;
					border-color: #000001;
					border-style: solid;
					padding: 0px;
					background: #fff;
					height: 150px;
					text-align: center;
					}
				
				#A1{
					
					display: block;
					margin-left: ;
					margin-right: ;
					width: 59.4%;
					overflow: hidden;
					height: 400px;
					margin: 0px;
					border-width: 0px;
					border-color: #000001;
					border-style: solid;
					padding-top: 5px;
					padding-bottom: 5px;
					padding-left: 8px;
					padding-right: 2px;
					}
					
					#A1 article h1{
						font-size: 1.5em;
						}
				
				#A2{
					display: block;
					margin-left: auto;
					margin-right: auto;
					width: 38%;
					height: 400px;
					position: relative;
					right: 0px;
					left: 604px;
					top: -414px;
					bottom: 0px;
					float: ;
					overflow: hidden;
					margin: 0px;
					border-width: 0px;
					border-color: #000001;
					border-style: solid;
					padding: 5px;
					}
					
					#A2 h1{
						font-size: 1em;						
						}
				
					#A2 aside article.A2_1{
						margin: 0px;
						border-width: 0px;
						border-color: #000001;
						border-style: solid;
						padding: 2px;
						width: ;
						height: 194px;
						}
					
											
					#A2 aside article.A2_2{
						margin: 0px;
						border-width: 0px;
						border-color: #000001;
						border-style: solid;
						padding: 2px;
					
						height: 194px;
						}
				
				#B{
					margin: 0px;
					border-width: 0px;
					border-color: #000001;
					border-style: solid;
					padding: 5px;
					width: ;
					height: 400px;
					clear: both;
					position: relative;
					right: 0px;
					left: 0px;
					top: -414px;
					bottom: 0px;
					-webkit-column-count: 3;
					-moz-column-count: 3;
					column-count: 3;
					-webkit-column-height: 300px;
					-moz-column-height: 300px;
					column-height: 300px;
					}
					
					#B h1{
						font-size: 1.1em;
						}
						
				#C{
					margin: 0px;
					border-width: 0px;
					border-color: #000001;
					border-style: solid;
					padding: 5px;
					clear: both;
					width: ;
					height: 400px;
					position: relative;
					right: 0px;
					left: 0px;
					top: -414px;
					bottom: 0px;
					-webkit-column-count: 3;
					-moz-column-count: 3;
					column-count: 3;
					-webkit-column-gap: 5px;
					-moz-column-gap: 5px;
					column-gap: 5px;
					}
				
					#C h1{
						font-size: 1.5em;
						}
						
				#D{
					margin: 0px;
					border-width: 0px;
					border-color: #000001;
					border-style: solid;
					padding: 5px;
					clear: both;
					width: ;
					height: 146px;
					position: relative;
					right: 0px;
					left: 0px;
					top: -414px;
					bottom: 0px;
					float: ;
					}
				
			footer{
				font-family: verdana, sans-serif;
				font-size: 75%;
				background: #fff;
				clear: both;
				margin-bottom: 2px;
				border-width: 0px;
				border-color: #000001;
				border-style: solid;
				padding: 5px;
				text-align: center;
				}				
		</style>
		
		<!--[if lt IE9]>
		<script scr="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
		<![end if]-->
				
	</head>
	<body>
		<div id="chapeaux">
			<img src="http://arbitragesportsanalytics.files.wordpress.com/2014/04/the-daily-arbitrage-logo-large-white-background11.png" alt="logo" width="200px" height="30px">
			<section>
				<form>
					<input type="search" id="s" name="s">
					<input type="submit" value="search">
				</form>
			</section>	
			
			<section>
				<ul>
					<li><a href="C:/Users/Pablo/Documents/Pablo/C/Pages/Wario sam/contact.html">Sing Up</a></li>
					<li><a href="http://www.google.com/">Log in</a></li>
				</ul>
			</section>
		</div>

		<header>
			<nav>
				<ul>
					<li><a href="/">Home</a></li>
					<li><a href="https://.../nfl" title="">NFL</a></li>
					<li><a href="http://.../nba">NBA</a></li>
					<li><a class="longer" href="http://.../fifa">World Cup</a></li>
					<li><a href="http://.../nhl">NHL</a></li>
					<li><a href="http://.../mlb">MLB</a></li>
					<li><a href="http://.../golf">Golf</a></li>
					<li><a href="http://.../ufc">UFC</a></li>
					<li><a href="http://.../more">More</a></li>
				</ul>				
			</nav>
		</header>

		<div id="slider"> <!--javascript code to be added-->
			<article>
				<img src="" alt="slide" width="280px" height="150px">	
				<img src="data:image/jpeg;base64,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" alt="Java Animation" width="280px" height="150px">				
				<img src="" alt="slide" width="280px" height="150px">				
			</article>
		</div>
		
		<div id="Main">
			<div id="A1">
				<article>
					<h1>Basic Bomb of Info</h1>
					<img src="http://i2.cdn.turner.com/nba/nba/dam/assets/140616105850-game-5-mini-movie-montage-no-multimedia-use-061614.home-t3.jpg" alt="info" width="580px" height="320px">
						Reference Lorem Ipsum, giving information on its origins,
						as well as a random Lipsum generator.
				</article>
			</div>

			<div id="A2">
				<aside>
					<article class="A2_1">
						<h1>Breaking news</h1>
						<img src="http://paulstory.ca/assets/Uploads/work-in-progress.png"	width="372px" height="171px">
					</article>
					
					<article class="A2_2">
						<h1>Breaking news</h1>
						<img src="http://paulstory.ca/assets/Uploads/work-in-progress.png"	alt="add" width="372px" height="171px">						
					</article>
				</aside>
			</div>
			
			<div id="B">
				<div id="B1">
					<article>
						<h1>Breaking news</h1>
						<img src="http://images.sodahead.com/polls/001952741/4658540924_work_in_progress_answer_6_xlarge.gif" width="310px" height="161px">	
														
					</article>
					
					<article>
						<h1>Breaking news</h1>
						<img src="http://jasonhelfenbaum.com/wp-content/uploads/2011/09/imWorkingOnIt1.jpg" width="310px" height="161px">	
														
					</article>
				</div>
				
				<div id="B2">
					<article>
						<h1>Breaking news</h1>
						<img src="http://images.sodahead.com/polls/001952741/4658540924_work_in_progress_answer_6_xlarge.gif" width="310px" height="161px">	
														
					</article>
					
					<article>
						<h1>Breaking news</h1>
						<img src="http://jasonhelfenbaum.com/wp-content/uploads/2011/09/imWorkingOnIt1.jpg" width="310px" height="161px">	
														
					</article>
				</div>
				
				<div id="B3">
					<article>
						<h1>Breaking news</h1>
						<img src="http://i2.cdn.turner.com/nba/nba/dam/assets/140616111035-kawhi-leonard-patty-mills-boris-diaw-spurs-bench.home-t6.jpg" width="310px" height="161px">	
														
					</article>
					
					<article>
						<h1>Breaking news</h1>
						<img src="http://jasonhelfenbaum.com/wp-content/uploads/2011/09/imWorkingOnIt1.jpg" width="310px" height="161px">	
														
					</article>
				</div>
			</div>
			
			<div id="C">
				<div id="C1">
					<article>
						<h1>News and Info</h1>
						<img src="http://www.chicagonow.com/cancer-is-not-a-gift/files/2013/05/work.jpg" width="320px" height="300px">
							Lorem Ipsum, as well as a random Lipsum generator.
					</article>
				</div>
				
				<div id="C2">
					<article>
						<h1>News and Info</h1>
						<img src="http://3.bp.blogspot.com/_4KXfWAeYK2A/TSI4hnmME6I/AAAAAAAANiU/0WpAhHL00hY/s1600/InProgress.jpg" width="320px" height="300px">
							Lorem Ipsum, as well as a random Lipsum generator.
					</article>
				</div>
				
				<div id="C3">
					<article>
						<h1>News and Info</h1>
						<img src="http://www.chicagonow.com/cancer-is-not-a-gift/files/2013/05/work.jpg" width="320px" height="300px">
							Lorem Ipsum, as well as a random Lipsum generator.
					</article>
				</div>
				
			</div>
			
			<div id="D">
				<aside>
					<h1>Get Social</h1>
					"D'z" section is a paragraph recovering information about<br>
					featuring options, like social networks, faybu, twtrr,<br>
					and so on...It could be also used for blogging and <br>
					live web-users interactions.<br>
					<em>not to bore audiences</em>
				</aside>
			</div>
			
		</div> <!--final Main-->

		<footer>
			<section>
			Made by<br> 
			This I reserve for info about us,8working4wario9sam.
		
			</section>
			<section>
			Copyright<br>
			The legal and so necessary section around
			everything of IP rights.
			</section>
		</footer>

		<script src="/"> <!--Java begins here-->
		
		</script>
	</body>
</html>

"""

class MainPage(webapp2.RequestHandler):

    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

