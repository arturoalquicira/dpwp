# single line comments

'''
multiple lined comments
Arturo Alquicira
may 5th 2014
DPWP
'''

first_name = 'Kermit'
last_name = 'Da Frog'

# -= *= += /=   ---> assignment operators

year_born = 1965
age = 2014 - year_born
# print age

'''
if(year_born < 1990){
    print 'you are part of generation y'
}

'''

# conditionals

if year_born > 1990:
    print 'you are part of generation y'
elif year_born < 1978:
    print 'you are part og generation x'
else:
    print 'you are from another planet'


print 'this is outside of the conditional statement'


# arrays
students = ['AUSTINE','arturo', 'chris', 'nicole', 'rebecca']
students.append('eddie')
students[0]= students[0].lower()
print students



# dictionaries - associative arrays
class_info = dict()
class_info = {'students': students, 'roster count': 9, 'room': 'fsa4a137'}
print class_info['roster count']


# loops
for s in students:
    print s + ', you will do great in this class!'
    if s == 'chris':
        break


# for i in range (start, end, incr/decr)
for i in range(0, 4, 2):
    print students[i]

# random numbers
import random

for i in range(0, 10):
    print random.randrange(2000)

# function
def calc_area(h, w):
    area = h * w
    return area

a = calc_area(6, 8)
print a

print calc_area(3, 20)

# format string method
user_name = 'Kermit'
join_date = 2001
message = '''
Welcome to our site, {user_name}!
You've been with us since {join_date}!
'''

message= message.format(**locals())
print message

# getting info from the user
first_name= raw_input('Type your first name')

print first_name + ', nice to meet you'





























