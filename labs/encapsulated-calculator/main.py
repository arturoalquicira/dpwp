
import webapp2
from musicFest import MusicFest
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        coachella = MusicFest()
        coachella.name = "Coachella Music Valley Fest"
        coachella.city = "Indio"
        coachella.state = "California"
        coachella.date = "15 - 17, April"
        coachella.hotel_name = "Hard Rock Cafe"
        coachella.__hotel_price = 600
        coachella.__flying_ticket = 350
        coachella.__airport_shuttle = 100
        coachella.__GA_tickets = 250
        coachella.__travel_insurance = 150
        
        lollapalooza = MusicFest()
        lollapalooza.name = "Lollapalooza"
        lollapalooza.city = "Chicago"
        lollapalooza.state = "Illinoise"
        lollapalooza.date = "1 - 3, August"
        lollapalooza.hotel_name = "Burnham Hotel"
        lollapalooza.__hotel_price = 500
        lollapalooza.__flying_ticket = 300
        lollapalooza.__airport_shuttle = 0
        lollapalooza.__GA_tickets = 250
        lollapalooza.__travel_insurance = 150

        bonnaroo = MusicFest()
        bonnaroo.name = "Bonnaroo"
        bonnaroo.city = "Manchester"
        bonnaroo.state = "Tennessee"
        bonnaroo.date = "12 - 15, July"
        bonnaroo.hotel_name = "Camping"
        bonnaroo.__hotel_price = 150
        bonnaroo.__flying_ticket = 300
        bonnaroo.__airport_shuttle = 120
        bonnaroo.__GA_tickets = 280
        bonnaroo.__travel_insurance = 150
        
        sxsw = MusicFest()
        sxsw.name = "SXSW - Music, Film & Interactive"
        sxsw.city = "Austin"
        sxsw.state = "Texas"
        sxsw.date = "13 - 15, July"
        sxsw.hotel_name = "Embassy Suites"
        sxsw.__hotel_price = 300
        sxsw.__flying_ticket = 250
        sxsw.__airport_shuttle = 100
        sxsw.__GA_tickets = 250
        sxsw.__travel_insurance = 150

        outside_lands = MusicFest()
        outside_lands.name = "Outside Lands - Music, Film & Interactive"
        outside_lands.city = "San Francisco"
        outside_lands.state = "California"
        outside_lands.date = "8 - 10, August"
        outside_lands.hotel_name = "Hotel Abri"
        outside_lands.__hotel_price = 350
        outside_lands.__flying_ticket = 350
        outside_lands.__airport_shuttle = 100
        outside_lands.__GA_tickets = 250
        outside_lands.__travel_insurance = 150


class Page(object):
    def __init__(self):
        self.__title = "Home"
        self.page_open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
    </head>
<body>
        '''
        self.page_content = '''
        '''
        self.page_close = '''
</body>
</html>
        '''


        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
