
import webapp2
from musicFest import MusicFest


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.coachella = MusicFest()
        self.coachella.name = "Coachella Music Valley Fest"
        self.coachella.city = "Indio"
        self.coachella.state = "California"
        self.coachella.date = "15 - 17, April"
        self.coachella.hotel_name = "Hard Rock Cafe"
        self.coachella.hotel_price = 600
        self.coachella.flying_ticket = 350
        self.coachella.airport_shuttle = 100
        self.coachella.ga_tickets = 250
        self.coachella.travel_insurance = 150
        self.coachella.total = self.coachella.total_cost()
        # print coachella.total

        self.lollapalooza = MusicFest()
        self.lollapalooza.name = "Lollapalooza"
        self.lollapalooza.city = "Chicago"
        self.lollapalooza.state = "Illinoise"
        self.lollapalooza.date = "1 - 3, August"
        self.lollapalooza.hotel_name = "Burnham Hotel"
        self.lollapalooza.hotel_price = 500
        self.lollapalooza.flying_ticket = 300
        self.lollapalooza.airport_shuttle = 0
        self.lollapalooza.ga_tickets = 250
        self.lollapalooza.travel_insurance = 150
        self.lollapalooza.total = self.lollapalooza.total_cost()
        # print lollapalooza.total

        self.bonnaroo = MusicFest()
        self.bonnaroo.name = "Bonnaroo"
        self.bonnaroo.city = "Manchester"
        self.bonnaroo.state = "Tennessee"
        self.bonnaroo.date = "12 - 15, July"
        self.bonnaroo.hotel_name = "Camping"
        self.bonnaroo.hotel_price = 150
        self.bonnaroo.flying_ticket = 300
        self.bonnaroo.airport_shuttle = 120
        self.bonnaroo.ga_tickets = 280
        self.bonnaroo.travel_insurance = 150
        self.bonnaroo.total = self.bonnaroo.total_cost()
        
        self.sxsw = MusicFest()
        self.sxsw.name = "SXSW - Music, Film & Interactive"
        self.sxsw.city = "Austin"
        self.sxsw.state = "Texas"
        self.sxsw.date = "13 - 15, July"
        self.sxsw.hotel_name = "Embassy Suites"
        self.sxsw.hotel_price = 300
        self.sxsw.flying_ticket = 250
        self.sxsw.airport_shuttle = 100
        self.sxsw.ga_tickets = 250
        self.sxsw.travel_insurance = 150
        self.sxsw.total = self.sxsw.total_cost()

        self.outside_lands = MusicFest()
        self.outside_lands.name = "Outside Lands - Music, Film & Interactive"
        self.outside_lands.city = "San Francisco"
        self.outside_lands.state = "California"
        self.outside_lands.date = "8 - 10, August"
        self.outside_lands.hotel_name = "Hotel Abri"
        self.outside_lands.hotel_price = 350
        self.outside_lands.flying_ticket = 350
        self.outside_lands.airport_shuttle = 100
        self.outside_lands.ga_tickets = 250
        self.outside_lands.travel_insurance = 150
        self.outside_lands.total = self.outside_lands.total_cost()

        page = Page()

        if self.request.GET:
            festivals = self.request.GET['fest']
            festival = str(festivals)
            self.response.write(self.print_out_content(festival))
        else:
            self.response.write(page.print_out_links())

    def print_out_content(self, festival=""):
        page = Page()

        if festival == '':
            pass
        else:
            self.title = festival.upper()
            self.content='''
        <div class="col-md-7">
            <div class="row">
                <div class="col-md-6">
                    <h1>{self.'''+festival+'''.name}</h1>
                        <ul>
                            <li>{self.'''+festival+'''.city}, {self.'''+festival+'''.state}</li>
                            <li>{self.'''+festival+'''.date}</li>
                        </ul>
                </div>
                <div class="col-md-5 col-md-offset-1">
                    <img src="images/'''+festival+'''.png" class="img-responsive img-thumbnail" alt="Responsive image">
                </div>
            </div>

            <table id="table_costs" class="table table-striped">
                <tr>
                    <th>Includes</th>
                    <th>Cost</th>
                </tr>
                <tr>
                    <td>Hotel ({self.'''+festival+'''.hotel_name})</td>
                    <td>${self.'''+festival+'''.hotel_price}</td>
                </tr>
                <tr>
                    <td>Flying Tickets</td>
                    <td>${self.'''+festival+'''.flying_ticket}</td>
                </tr>
                <tr>
                    <td>Airport Shuttle</td>
                    <td>${self.'''+festival+'''.airport_shuttle}</td>
                </tr>
                <tr>
                    <td>Festival Tickets(GA)</td>
                    <td>${self.'''+festival+'''.ga_tickets}</td>
                </tr>
                <tr>
                    <td>Travel Insurance</td>
                    <td>${self.'''+festival+'''.travel_insurance}</td>
                </tr>
                <tr>
                    <td><strong>Total</strong></td>
                    <td><strong>${self.'''+festival+'''.total}</strong></td>
                </tr>
            </table>
        </div>
    </div>'''
            self.all = page.page_open + page.page_links + self.content + page.page_close
            return self.all.format(**locals())



class Page(object):
    def __init__(self):
        self.title = "On Stage Tours"
        self.page_open = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{self.title}</title>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
<div class="container-fluid">
    <div class="row">
        <div class="col-md-3 col-md-offset-1">
            <h1>On Stage Tours!</h1>
        </div>
    </div>
    <div class="row">
        <div class="col-md-9 col-md-offset-1">
            <p>When we started, we had a thirst for something other than just another watered down tour experience.
                We itched to go to real music festivals - we hungered to find the world's wildest parties. So when the
                time came we gave our tours a little bit of a twist - and became the pioneers of tours to music festivals.

                We sought out the big guns Coachella and Lollapalooza - both universally regarded as the ultimate
                festivals, year in and out attracting the biggest names in the business. Imagine watching the afternoon
                desert sunset at Coachella. Or singing on Outside Lands in San Francisco, sunning yourself at Bonnaroo or even partying
                at SXSW. Half the fun isn't even the festival destination - it's the adventures along the way.
            </p>
        </div>
    </div>
        '''
        self.page_links = '''
    <div class="row">
        <div class="col-md-3 col-md-offset-1">
            <h2>Music Festivals</h2>
            <div class="list-group">
                <a href="?fest=coachella" class="list-group-item active">
                    <h4 class="list-group-item-heading">Coachella</h4>
                </a>
                <a href="?fest=lollapalooza" class="list-group-item ">
                    <h4 class="list-group-item-heading">Lollapalooza</h4>
                </a>
                <a href="?fest=bonnaroo" class="list-group-item ">
                    <h4 class="list-group-item-heading">Bonnaroo</h4>
                </a>
                <a href="?fest=sxsw" class="list-group-item ">
                    <h4 class="list-group-item-heading">SXSW</h4>
                </a>
                <a href="?fest=outside_lands" class="list-group-item ">
                    <h4 class="list-group-item-heading">Outside Lands</h4>
                </a>
            </div>
        </div>
        '''
        self.page_content = ''

        self.page_close = '''
</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</body>
</html>

        '''
        self.all = ""

    def print_out_links(self, content=""):
        self.all = self.page_open + self.page_links + content + self.page_close
        self.all = self.all.format(**locals())
        return self.all





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)



