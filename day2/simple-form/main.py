
import webapp2
# from FILE import CLASSNAME
from page import Page
# blueprint for creating our web app
class MainHandler(webapp2.RequestHandler):
    # catalyst, starts our web app
    def get(self):

        p = Page() #calls constructor init function inside Page class
        # attributes:
            # instance.attribute

        # methods:
            # instance.method()

        if self.request.GET:
            fn = self.request.GET['firstname']
            ln = self.request.GET['lastname']
            self.response.write(p.print_out(fn + ' ' + ln))
        else:
            self.response.write(p.print_out(''))

        # attribute:
        # self.response.write(p.page_open + p.page_content + p.page_close)
        # or
        # method:
        # self.response.write(p.print_out('All your base are belong to us!'))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
