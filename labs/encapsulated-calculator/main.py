
import webapp2
from musicFest import MusicFest


class MainHandler(webapp2.RequestHandler):
    def get(self):

        page = Page()
        self.response.write(page.all)

        coachella = MusicFest()
        coachella.name = "Coachella Music Valley Fest"
        coachella.city = "Indio"
        coachella.state = "California"
        coachella.date = "15 - 17, April"
        coachella.hotel_name = "Hard Rock Cafe"
        coachella.hotel_price = 600
        coachella.flying_ticket = 350
        coachella.airport_shuttle = 100
        coachella.ga_tickets = 250
        coachella.travel_insurance = 150
        coachella.total = coachella.total_cost()
        # print coachella.total

        lollapalooza = MusicFest()
        lollapalooza.name = "Lollapalooza"
        lollapalooza.city = "Chicago"
        lollapalooza.state = "Illinoise"
        lollapalooza.date = "1 - 3, August"
        lollapalooza.hotel_name = "Burnham Hotel"
        lollapalooza.hotel_price = 500
        lollapalooza.flying_ticket = 300
        lollapalooza.airport_shuttle = 0
        lollapalooza.ga_tickets = 250
        lollapalooza.travel_insurance = 150
        lollapalooza.total = lollapalooza.total_cost()
        # print lollapalooza.total

        bonnaroo = MusicFest()
        bonnaroo.name = "Bonnaroo"
        bonnaroo.city = "Manchester"
        bonnaroo.state = "Tennessee"
        bonnaroo.date = "12 - 15, July"
        bonnaroo.hotel_name = "Camping"
        bonnaroo.hotel_price = 150
        bonnaroo.flying_ticket = 300
        bonnaroo.airport_shuttle = 120
        bonnaroo.ga_tickets = 280
        bonnaroo.travel_insurance = 150
        
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
        self.title = "Live Tours"
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
        self.page_links = '''
        <ul>
            <li><a href="?fest=coachella">Coachella</a></li>
            <li><a href="?fest=lollapalooza">Lollapalooza</a></li>
            <li><a href="?fest=bonnaroo">Bonnaroo</a></li>
            <li><a href="?fest=sxsw">SXSW</a></li>
            <li><a href="?fest=outside_lands">Outside Lands</a></li>
        </ul>

        '''
        self.page_close = '''
</body>
</html>
        '''

        self.all = self.page_open + self.page_content + self.page_links + self.page_close
        self.all = self.all.format(**locals())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
