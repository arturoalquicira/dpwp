'''
Name: Arturo Alquicira
Quiz 1

DPWP

'''


# Functions and conditionals

input_width = raw_input('Width:')
input_height = raw_input('Height:')

def calc_area(w, h):
    a = w*h
    return a

area = calc_area(int(input_width), int(input_height))

if input_width == input_height:
    print 'The area of your square is ' + str(area) + ' square feet.'
else:
    print 'The area of your rectangle is ' + str(area) + ' square feet.'

# Functions and loops


def count_down():
    bottles = 99
    for b in range(bottles, 0, -1):
        bottles -= 1
        print str([b]) + ' Bottles of Beer on the Wall, ' + str([b]) + ' Bottles of Beer... take one down and pass it ' \
       'around. Now you have ' + str([bottles]) + ' bottles of beer on the wall.'

count_down()




