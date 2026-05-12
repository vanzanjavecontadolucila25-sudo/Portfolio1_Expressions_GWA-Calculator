##Read Me: In fulfillment for the subject BES 10a, this project is a Python-based General Weighted Average (GWA) Calculator that computes students’ GWA using grades and subject units. It demonstrates basic programming concepts such as variables, input and output, expressions, arithmetic operations, type conversion, sequential programming, and the use of print statement.##

##This is the title section##
print ('========General Weighted Average (GWA) Calculator==============')
print ('Note: Input only numerical values and zeroes for placeholders.')

##For any section in the page containing "print ('')", expect it to be a page break/space##
print ('')

##This section acquires the data needed for computation from users' inputs##
#For each subject the number of units and grade are required
sub1=input('Grade Sub1: ')
unitsub1=input('Unit Sub1: ')
print ('')

sub2=input('Grade Sub2: ')
unitsub2=input('Unit Sub2: ')
print ('')

sub3=input('Grade Sub3: ')
unitsub3=input('Unit Sub3: ')
print ('')

sub4=input('Grade Sub4: ')
unitsub4=input('Unit Sub4: ')
print ('')

sub5=input('Grade Sub5: ')
unitsub5=input('Unit Sub5: ')
print ('')

sub6=input('Grade Sub6: ')
unitsub6=input('Unit Sub6: ')
print ('')

sub7=input('Grade Sub7: ')
unitsub7=input('Unit Sub7: ')
print ('')

sub8=input('Grade Sub8: ')
unitsub8=input('Unit Sub8: ')
print ('')

sub9=input('Grade Sub9: ')
unitsub9=input('Unit Sub9: ')
print ('')

sub10=input('Grade Sub10: ')
unitsub10=input('Unit Sub10: ') 
print ('')

##This section converts the string inputs into float for computation##
GSub1=float(sub1)
USub1=float(unitsub1)

GSub2=float(sub2)
USub2=float(unitsub2)

GSub3=float(sub3)
USub3=float(unitsub3)

GSub4=float(sub4)
USub4=float(unitsub4)

GSub5=float(sub5)
USub5=float(unitsub5)

GSub6=float(sub6)
USub6=float(unitsub6)

GSub7=float(sub7)
USub7=float(unitsub7)

GSub8=float(sub8)
USub8=float(unitsub8)

GSub9=float(sub9)
USub9=float(unitsub9)

GSub10=float(sub10)
USub10=float(unitsub10)

#The total / combined units are acquired using:
totalunits= USub1 + USub2 + USub3 + USub4 + USub5 + USub6 + USub7 + USub8 + USub9 + USub10

##This section calculates the data using the formula for gwa##
#This formula is acquired from NEUST Honor Society in facebook
#source link: https://www.facebook.com/share/p/1AUkfx9J9p/
Dividend= (GSub1*USub1)+(GSub2*USub2)+(GSub3*USub3)+(GSub4*USub4)+(GSub5*USub5)+(GSub6*USub6)+(GSub7*USub7)+(GSub8*USub8)+(GSub9*USub9)+(GSub10*USub10) 

gwa= Dividend/totalunits
#This shows the computed data to the users''
print ('===============================================================')
print ('            Your computed GWA is:', gwa)
print ('===============================================================')

##This section shows the equivalence of the gwa calculated as well as the adjectival rating##
#This table is acquired from Bicol Univeristy - University Student Council in facebook
#source link: https://www.facebook.com/share/p/1BaD4wxKb7/

print("---------------------------------------------------------------")
print("| Adjectival Rating |  Grade  |         Equivalence         |")
print("---------------------------------------------------------------")
print("| Outstanding       | 1.0     | 99-100                      |")
print("| Outstanding       | 1.1     | 98                          |")
print("| Outstanding       | 1.2     | 97                          |")
print("| Outstanding       | 1.3     | 96                          |")
print("| Outstanding       | 1.4     | 95                          |")
print("| Superior          | 1.5     | 94                          |")
print("| Superior          | 1.6     | 93                          |")
print("| Superior          | 1.7     | 92                          |")
print("| Very Satisfactory | 1.8     | 91                          |")
print("| Very Satisfactory | 1.9     | 90                          |")
print("| Very Satisfactory | 2.0     | 89                          |")
print("| Very Satisfactory | 2.1     | 88                          |")
print("| Very Satisfactory | 2.2     | 87                          |")
print("| Very Satisfactory | 2.3     | 86                          |")
print("| Very Satisfactory | 2.4     | 85                          |")
print("| Very Satisfactory | 2.5     | 84                          |")
print("| Satisfactory      | 2.6     | 82-83                       |")
print("| Satisfactory      | 2.7     | 80-81                       |")
print("| Satisfactory      | 2.8     | 78-79                       |")
print("| Fair / Average    | 2.9     | 76-77                       |")
print("| Fair / Average    | 3.0     | 75 (Passing)                |")
print("| Poor              | 3.1-4.0 | Below 75 Conditional        |")
print("| Failure           | 5.0     | Failure                     |")
print("---------------------------------------------------------------")

print ('')
##This section is the closing statement for motivation##
#quote taken from: https://www.parents.com/kids/education/back-to-school/back-to-school-quotes-to-get-kids-excited-for-class/
print ('You did well no matter the outcome!')
print ('Always remember:')
print ('Work hard, be kind, and amazing things will happen.')
print ("          - Conan O'brien")



