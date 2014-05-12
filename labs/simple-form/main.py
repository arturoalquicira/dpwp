'''
Name: Arturo Alquicira
Lab 2: Simple Form

DPWP

'''

import webapp2
from form import Form
class MainHandler(webapp2.RequestHandler):
    def get(self):

        form = Form()
        if self.request.GET:
            username = self.request.GET['username']
            password = self.request.GET['password']
            email = self.request.GET['email']
            first_name = self.request.GET['firstname']
            last_name = self.request.GET['lastname']
            sex = self.request.GET['sex']
            address = self.request.GET['address']
            city = self.request.GET['city']
            state = self.request.GET['state']
            country = self.request.GET['country']
            zip = self.request.GET['zip']

            self.response.write(form.print_result(
                '<p><strong>Username: </strong>' + username + '</p>'
                '<p><strong>Password: </strong>' + password + '</p>'
                '<p><strong>E-mail: </strong>' + email + '</p>'
                '<p><strong>First Name: </strong>' + first_name + '</p>'
                '<p><strong>Last Name: </strong>' + last_name + '</p>'
                '<p><strong>Genre: </strong>' + sex + '</p>'
                '<p><strong>Address: </strong>' + address + '</p>'
                '<p><strong>City: </strong>' + city + '</p>'
                '<p><strong>State: </strong>' + state + '</p>'
                '<p><strong>Country: </strong>' + country + '</p>'
                '<p><strong>Zip Code: </strong>' + zip + '</p>'
            ))
        else:
            self.response.write(form.print_content(''))







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
