import sys
import optparse

def get_args():
	parse=optparse.OptionParser()
	parse.add_option("-f","--first",dest="x",help="First value")
	parse.add_option("-s","--second",dest="y",help="Second value")
	return parse.parse_args()

(options,arguments)=get_args()
x=int(options.x)
y=int(options.y)

print(x+y)

print('Count:', len(sys.argv))          ### This the main part where we the arguments list .....
print('Type:', type(sys.argv))

for arg in sys.argv:
    print('Argument:', arg)
