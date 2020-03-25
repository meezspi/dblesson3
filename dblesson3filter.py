import webapp2
from google.appengine.ext import db

mylimit='5'
# Create a KIND called "Comment" (like a table)
class Comment(db.Model):
    content = db.StringProperty(multiline=True)
    rank = db.StringProperty()

class MainPage(webapp2.RequestHandler):

    def get(self):
	# Create the FORM
	self.response.write('<html><body><h1>Bad Tomatoes</h1>')
	self.response.write(""" <hr> <form method="post">
	Enter the MOVIE:
	<input type="textarea" name="mypost"></input>
	<p>and RANK (1-10):
	<input type="textarea" name="rank"></input><p>
	<p>INPUT a limit for ranks (1-10) above which the movies will be displayed:
	<input type="textarea" name="limit"></input><p>
	<input type="submit"></input>
	</form>""")
	self.response.write('</body></html>')

    def post(self):
	# get what the user entered in the FORM
	content_entered = self.request.get('mypost')
	rank_entered = self.request.get('rank')
	mylimit = self.request.get('limit')
	# STORE it to the content of an entity of Comment table/kind
	mycomment = Comment(content=content_entered,rank=rank_entered)
	mycomment.put()
	
	# Create the REPLY web page	
	self.response.write('<html><body><h1>Reviews</h1>')
	self.response.write('<hr> Previous reviews (filtered):')
	
	# Print ALL previous comments stored in Datastore

	# Get SOME entities of the "Comment" kind/table
	myquerry = Comment.all()
	# FILTER
	myquerry.filter("rank >",mylimit)
	# SORT /by ORDER
	myquerry.order("rank")
	for acomment in myquerry:
	    self.response.write('<p>%s = ' % acomment.rank)
	    self.response.write('%s</p>' % acomment.content)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
	
	
	

	