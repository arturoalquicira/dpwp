class MusicFest(object):
    def __init__(self):
        self.name = ""
        self.city = ""
        self.state = ""
        self.date = ""
        self.hotel_name = ""
        self.__hotel_price = 0
        self.__flying_ticket = 0
        self.__airport_shuttle = 0
        self.__GA_tickets = 0
        self.__travel_insurance = 0
        self.__total = self.__flying_ticket + self.__hotel_price + self.__travel_insurance + self.__GA_tickets + self.__airport_shuttle

    @property
    def hotel_price(self):
        return self.__hotel_price

    @hotel_price.setter
    def hotel_price(self, price):
        self.__hotel_price = price

    @property
    def flying_ticket(self):
        return self.__flying_ticket

    @flying_ticket.setter
    def flying_ticket(self, price):
        self.__flying_ticket = price

    @property
    def airport_shuttle(self):
        return self.__airport_shuttle

    @airport_shuttle.setter
    def airport_shuttle(self, price):
        self.__airport_shuttle = price

    @property
    def ga_ticket(self):
        return self.__GA_tickets

    @ga_ticket.setter
    def ga_ticket(self, price):
        self.__GA_tickets = price

    @property
    def travel_insurance(self):
        return self.__travel_insurance

    @travel_insurance.setter
    def travel_insurance(self, price):
        self.__travel_insurance = price

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, cost):
        self.__total = cost