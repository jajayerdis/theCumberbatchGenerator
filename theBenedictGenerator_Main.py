"""randomly generates a new variant of benedict cumberbatch."""
import sys
import random

def main():
    """Choose two names at random from a tuple and print to screen."""
    print( 'Welcome to the Benedict Cumberbatch generator\n' )
    print( 'Just like Benedict Cumberbatch but different\n' )
    first = ( 'Benedryl', 'BenneyBoop', 'Wimbledon', 'Frumious', 'Bendycat', 
    'Bandycoot', 'Buffalo', 'Breadmachine', 'Cucumber', 'Benevolent', 
    'Bumblebee', 'Benedict', 'Bulbasaur', 'Babadook', 'Bennyflip',
    'Englishman', 'Buttercup', 'Bentokit') 
    last = ( 'Appleyard', 'Hooperbag', 'Walkingstick', 'Baggageclaim', 'Computerglitch', 
    'Cummerbund', 'Bandersnatch', 'Crackerjack', 'Custardbath', 'Crashington', 
    'Cookiebatch', 'Windowspatch', 'Tennismatch','Cumberbop', 'Hairysnatch', 
    'Cabbagepatch', 'Cucumberbatch', 'Canterbury', 'Sillyname' ) 
    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        print( "\n\n" )
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print( "\n\n" )
        try_again = input( "\n\nTry Again? (Press Enter else n to quit)\n " )
        if try_again.lower() == "n":
            break 
    input('\nPress Enter to exit.')
if __name__ == "__main__":
    main()

