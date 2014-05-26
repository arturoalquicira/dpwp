'''

Animal super-class

'''

class AbstractAnimal(object):
    def __init__(self):
        self._name = ""
        self._sci_name = ""
        self._animal_class = ""
        self._order = ""
        self._family = ""
        self._genus = ""
        self._url = ""
        self._lifespan = 0
        self._habitat = ""
        self._geolocation = ""
        self.animal_sound = self.sound()

    ''' Getters and setters for the properties of the class '''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def sci_name(self):
        return self._sci_name

    @sci_name.setter
    def sci_name(self, sci):
        self._sci_name = sci

    @property
    def animal_class(self):
        return self._animal_class

    @animal_class.setter
    def animal_class(self, c):
        self._animal_class = c

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, o):
        self._order = o

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, f):
        self._family = f

    @property
    def genus(self):
        return self._genus

    @genus.setter
    def genus(self, g):
        self._genus = g

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, u):
        self._url = u

    @property
    def lifespan(self):
        return self._lifespan

    @lifespan.setter
    def lifespan(self, l):
        self._lifespan = l

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, h):
        self._habitat = h

    @property
    def geolocation(self):
        return self._geolocation

    @geolocation.setter
    def geolocation(self, g):
        self._geolocation = g

    def sound(self):  # method to overwrite each animal sound from their own sub-class
        return ""

''' sub-classes for each animal to inherit from the super-class "AbstractAnimal" '''


class RedFox(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)

    def sound(self):
        return "rrrrin-din-din rrrin din-din!!!"


class GrizzlyBear(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)

    def sound(self):
        return "grrroowll!!!"


class SiberianTiger(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)

    def sound(self):
        return "grrrrrrr!!!"


class HumboldtPenguin(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)

    def sound(self):
        return "quick-quiiiiick-quick!!!"
