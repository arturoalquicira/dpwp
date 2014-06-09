'''

Arturo Alquicira

Final Project - DPWP

'''
import webapp2
from page import *
import urllib2
import json
import math


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = FormPage()
        d_obj = DataObject()
        d_view = DataView()

        if self.request.GET:

            d_model = DataModel()
            code = str(self.request.GET['place'])
            d_model.place = code.replace(" ", '')
            d_model.checkin = str(self.request.GET['checkin'])
            d_model.checkout = str(self.request.GET['checkout'])
            d_model.request()

            d_view.array_view = d_model.data_obj.data_array

            lists = d_view.print_list()
            details = d_view.print_details()
            # self.response.write(page.open + details + page.nav_bar + page.filters + lists + page.close)
            self.response.write(page.page_lists(details, lists))



        else:
            self.response.write(page.page_home())




class DataModel(object):
    def __init__(self):
        self.__place = ""
        self.__checkin = ""
        self.__checkout = ""
        self.url = ""

    def request(self):
        self.url = "https://api.9flats.com/api/v4/places?client_id=VNIEHwEnIxP7UHfWl4tJkPz5utURSfGUSBcsi1AL&search[query]=" + self.__place + "&search[start_date]=" + self.__checkin + "&search[end_date]=" + self.__checkout + "&search[per_page]=100&search[page]=1"
        #  go get the api info
        req = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        opener.open(req)
        data = opener.open(req)

        #  parse it
        jsondoc = json.load(data)
        query = jsondoc['places']

        self.data_obj = DataObject()

        main_array = []

        for i in range(0, len(query), 1):
            name = jsondoc['places'][i]['place']['place_details']['name']
            name = name.encode('utf-8')
            city = jsondoc['places'][i]['place']['place_details']['city']
            country = jsondoc['places'][i]['place']['place_details']['country']
            number_of_beds = jsondoc['places'][i]['place']['place_details']['number_of_beds']
            number_of_bedrooms = jsondoc['places'][i]['place']['place_details']['number_of_bedrooms']
            number_of_bathrooms = jsondoc['places'][i]['place']['place_details']['number_of_bathrooms']
            minimum_nights = jsondoc['places'][i]['place']['place_details']['minimum_nights']
            maximum_nights = jsondoc['places'][i]['place']['place_details']['maximum_nights']
            category = jsondoc['places'][i]['place']['place_details']['category']
            place_type = jsondoc['places'][i]['place']['place_details']['place_type']
            house_rules = jsondoc['places'][i]['place']['place_details']['house_rules']
            description = jsondoc['places'][i]['place']['place_details']['description']
            description = description.encode('utf-8')
            price = jsondoc['places'][i]['place']['pricing']['price']
            price = str(price)
            currency = jsondoc['places'][i]['place']['pricing']['currency']
            pic1 = jsondoc['places'][i]['place']['place_details']['additional_photos'][0]['place_photo']['url']
            pic1 = pic1.replace('medium', 'large')
            pic2 = jsondoc['places'][i]['place']['place_details']['additional_photos'][1]['place_photo']['url']
            pic2 = pic2.replace('medium', 'large')
            pic3 = jsondoc['places'][i]['place']['place_details']['additional_photos'][2]['place_photo']['url']
            pic3 = pic3.replace('medium', 'large')

            results_arr = {
                'name': name,
                'city': city,
                'country': country,
                'number_of_beds': number_of_beds,
                'number_of_bathrooms': number_of_bathrooms,
                'number_of_bedrooms': number_of_bedrooms,
                'min_nights': minimum_nights,
                'max_nights': maximum_nights,
                'category': category,
                'place_type': place_type,
                'house_rules': house_rules,
                'description': description,
                'price': price,
                'currency': currency,
                'pic1': pic1,
                'pic2': pic2,
                'pic3': pic3
            }

            main_array.append(results_arr)

        self.data_obj.data_array = main_array



    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, p):
        self.__place = p

    @property
    def checkin(self):
        return self.__checkin

    @checkin.setter
    def checkin(self, i):
        self.__checkin = i

    @property
    def checkout(self):
        return self.__checkout

    @checkout.setter
    def checkout(self, o):
        self.__checkout = o

        
class DataView(object):
    def __init__(self):

        self.array_view = []
        self.list = ""
        self.details = ""
        self.counter = 0
        self.counter2 = 0
        self.id_modal = 1
        self.id_modal2 = 2

    def print_list(self):
        for i, k in zip(self.array_view[0::2], self.array_view[1::2]):
            self.counter += 1
            self.counter2 += 2

            self.list += '''

            <div class="row" id="content-row">
                <div class="col-md-5 res-info" >
                    <h4 class="res-title">''' + str(i['name']) + '''</h4>
                    <div id="carousel-example-generic'''+str(self.counter)+'''" class="carousel slide" data-ride="carousel" data-interval="false">
                        <!-- Indicators -->
                        <ol class="carousel-indicators">
                            <li data-target="#carousel-example-generic'''+str(self.counter)+'''" data-slide-to="0" class="active"></li>
                            <li data-target="#carousel-example-generic'''+str(self.counter)+'''" data-slide-to="1"></li>
                            <li data-target="#carousel-example-generic'''+str(self.counter)+'''" data-slide-to="2"></li>
                        </ol>

                        <!-- Wrapper for slides -->
                        <div class="carousel-inner">
                            <div class="item active">
                                <img src="http:''' + str(i['pic1']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                            <div class="item ">
                                <img src="http:''' + str(i['pic2']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                            <div class="item ">
                                <img src="http:''' + str(i['pic3']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                        </div>

                        <!-- Controls -->
                        <a class="left carousel-control res-img-corner" href="#carousel-example-generic'''+str(self.counter)+'''" data-slide="prev">
                        <span class="glyphicon glyphicon-chevron-left"></span>
                        </a>
                        <a class="right carousel-control res-img-corner" href="#carousel-example-generic'''+str(self.counter)+'''" data-slide="next">
                        <span class="glyphicon glyphicon-chevron-right"></span>
                        </a>
                    </div>
                    <hr>
                    <div class="row" >
                        <div class="col-md-12">
                            <div class="row">
                                <div class="col-md-6">
                                    <p>''' + str(i['city']) + ''', ''' + str(i['country']) + '''</p>
                                    <p><strong>Category: </strong>''' + str(i['category']) + '''</p>
                                    <p><strong>Place Type: </strong>''' + str(i['place_type']) + '''</p>
                                </div>
                                <div class="col-md-6">
                                    <h3 class="text-right">$''' + str(i['price']) + ''' ''' + str(i['currency']) + '''</h3>
                                </div>
                            </div>
                            <button type="button" class="btn btn-default btn-lg btn-block" data-toggle="modal" data-target="#details-''' + str(self.id_modal) + '''">+ more info</button>
                            <button type="button" class="btn btn-primary btn-lg btn-block">Book It!</button>
                        </div>
                    </div>
                </div>


                <div class="col-md-5 col-md-offset-1 res-info" >
                    <h4 class="res-title">''' + str(k['name']) + '''</h4>
                    <div id="carousel-example-generics'''+str(self.counter2)+'''" class="carousel slide" data-ride="carousel" data-interval="false">
                        <!-- Indicators -->
                        <ol class="carousel-indicators">
                            <li data-target="#carousel-example-generics'''+str(self.counter2)+'''" data-slide-to="0" class="active"></li>
                            <li data-target="#carousel-example-generics'''+str(self.counter2)+'''" data-slide-to="1"></li>
                            <li data-target="#carousel-example-generics'''+str(self.counter2)+'''" data-slide-to="2"></li>
                        </ol>

                        <!-- Wrapper for slides -->
                        <div class="carousel-inner">
                            <div class="item active">
                                <img src="http:''' + str(k['pic1']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                            <div class="item ">
                                <img src="http:''' + str(k['pic2']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                            <div class="item ">
                                <img src="http:''' + str(k['pic3']) + '''" alt="..." class="img-rounded">
                                <div class="carousel-caption">
                                </div>
                            </div>
                        </div>

                        <!-- Controls -->
                        <a class="left carousel-control res-img-corner" href="#carousel-example-generics'''+str(self.counter2)+'''" data-slide="prev">
                        <span class="glyphicon glyphicon-chevron-left"></span>
                        </a>
                        <a class="right carousel-control res-img-corner" href="#carousel-example-generics'''+str(self.counter2)+'''" data-slide="next">
                        <span class="glyphicon glyphicon-chevron-right"></span>
                        </a>
                    </div>
                    <hr>
                    <div class="row" >
                        <div class="col-md-12">
                            <div class="row">
                                <div class="col-md-6">
                                    <p>''' + str(k['city']) + ''', ''' + str(k['country']) + '''</p>
                                    <p><strong>Category: </strong>''' + str(k['category']) + '''</p>
                                    <p><strong>Place Type: </strong>''' + str(k['place_type']) + '''</p>
                                </div>
                                <div class="col-md-6">
                                    <h3 class="text-right">$''' + str(k['price']) + ''' ''' + str(k['currency']) + '''</h3>
                                </div>
                            </div>
                            <button type="button" class="btn btn-default btn-lg btn-block" data-toggle="modal" data-target="#details-''' + str(self.id_modal2) + '''">+ more info</button>
                            <button type="button" class="btn btn-primary btn-lg btn-block">Book It!</button>
                        </div>
                    </div>
                </div>
            </div>

            '''
            self.id_modal += 2
            self.id_modal2 += 2
        return self.list

    def print_details(self):
        self.id_modals = 0

        for i in self.array_view:
            self.id_modals += 1
            self.details += '''
<div class="modal fade modal-details" id="details-''' + str(self.id_modals) + '''" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title" id="myModalLabel">''' + str(i['name']) + '''</h4>
                </div>
                <div class="modal-body">
                    <div id="carousel-example-modal''' + str(self.id_modals) + '''" class="carousel slide" data-ride="carousel" data-interval="false">
                                <!-- Indicators -->
                                <ol class="carousel-indicators">
                                    <li data-target="#carousel-example-modal''' + str(self.id_modals) + '''" data-slide-to="0" class="active"></li>
                                    <li data-target="#carousel-example-modal''' + str(self.id_modals) + '''" data-slide-to="1"></li>
                                    <li data-target="#carousel-example-modal''' + str(self.id_modals) + '''" data-slide-to="2"></li>
                                </ol>

                                <!-- Wrapper for slides -->
                                <div class="carousel-inner">
                                    <div class="item active">
                                        <img src="http:''' + str(i['pic1']) + '''" alt="..." class="img-rounded">
                                        <div class="carousel-caption">
                                        </div>
                                    </div>
                                    <div class="item ">
                                        <img src="http:''' + str(i['pic2']) + '''" alt="..." class="img-rounded">
                                        <div class="carousel-caption">
                                        </div>
                                    </div>
                                    <div class="item ">
                                        <img src="http:''' + str(i['pic3']) + '''" alt="..." class="img-rounded">
                                        <div class="carousel-caption">
                                        </div>
                                    </div>


                                </div>

                                <!-- Controls -->
                                <a class="left carousel-control res-img-corner" href="#carousel-example-modal''' + str(self.id_modals) + '''" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left"></span>
                                </a>
                                <a class="right carousel-control res-img-corner" href="#carousel-example-modal''' + str(self.id_modals) + '''" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right"></span>
                                </a>
                    </div> <!-- ends carousel -->
                    <hr>
                    <p><strong>Location: </strong>''' + str(i['city']) + ''', ''' + str(i['country']) + ''', 32792</p>
                    <p><strong>Category: </strong>''' + str(i['category']) + '''</p>
                    <p><strong>Place Type: </strong>''' + str(i['place_type']) + '''</p>
                    <p><strong>Minimum Nights: </strong>''' + str(i['min_nights']) + '''</p>
                    <p><strong>Maximum Nights: </strong>''' + str(i['max_nights']) + '''</p>
                    <hr>
                    <p><strong>Number of Beds: </strong>''' + str(i['number_of_beds']) + '''</p>
                    <p><strong>Number of Bedrooms: </strong>''' + str(i['number_of_bedrooms']) + '''</p>
                    <p><strong>Number of Bathrooms: </strong>''' + str(i['number_of_bathrooms']) + '''</p>
                    <ul>
                        <li><strong>Amenities: </strong>
                            <ul>
                                <li>Air conditioning</li>
                                <li>Dishwasher</li>
                                <li>Garden</li>
                                <li>Heating</li>
                                <li>Wi-Fi</li>
                                <li>TV</li>
                            </ul>
                        </li>
                    </ul>
                    <p><strong>Cleaning Fee: </strong>$25</p>
                    <hr>
                    <p><strong>House Rules: </strong>''' + str(i['house_rules']) + '''</p>
                    <div class="panel-group" id="accordion''' + str(self.id_modals) + '''">
                      <div class="panel panel-default">
                        <div class="panel-heading">
                          <h4 class="panel-title">
                            <a data-toggle="collapse" data-parent="#accordion''' + str(self.id_modals) + '''" href="#collapseOne''' + str(self.id_modals) + '''">
                              Description
                            </a>
                          </h4>
                        </div>
                        <div id="collapseOne''' + str(self.id_modals) + '''" class="panel-collapse collapse out">
                          <div class="panel-body"><span>''' + str(i['description']) + '''</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <hr>
                    <h2 class="text-right">$''' + str(i['price']) + ''' ''' + str(i['currency']) + '''</h2>
                    <p class="text-right">per night</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Book It!</button>
                </div>
            </div>
        </div>
</div> <!-- Ends Details view -->

            '''
        return self.details


class DataObject(object):
    def __init__(self):

        self.data_array = []






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
