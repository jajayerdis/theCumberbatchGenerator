import sys, random
print( 'Welcome to the Benedict Cumberbatch generator\n' )
print( 'A name just like Benedict Cumberbatch but different\n' )

first = ( 'Benedryl', 'BenneyBoop', 'Wimbledon', 'Frumious', 'Bendycat', 'Bandycoot', 'Buffalo', 
'Breadmachine', 'Cucumber', 'Benevolent', 'Bumblebee', 'Benedict', 'Bulbasaur', 'Babadook', 'Bennyflip',
'Englishman', 'Buttercup', 'Bentokit')

last = ( 'Appleyard', 'Hooperbag', 'Walkingstick', 'Baggageclaim', 'Computerglitch', 'Cummerbund', 
'Bandersnatch', 'Crackerjack', 'Custardbath', 'Crashington', 'Cookiebatch', 'Windowspatch', 'Tennismatch',
'Cumberbop', 'Hairysnatch', 'Cabbagepatch', 'Cucumberbatch', 'Canterbury', 'sillyname' ) 

while True:
    
    firstName = random.choice(first)
    lastName = random.choice(last)
    print( "\n\n" )
    print( "{} {}" .format(firstName, lastName), file = sys.stderr )
    print( "\n\n" )

    try_again = input( "\n\nTry Again? (Press Enter else n to quit)\n " )
    if try_again.lower() == "n":
        break
    input('\nPress Enter to exit.')
