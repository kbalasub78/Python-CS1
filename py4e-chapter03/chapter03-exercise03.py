print('Chapter 3 - Excerise 3')

import sys

# Get user input for score
try:
    score = float( input('Enter score (range from 0.0 to 1.0): ') )
except:
    print('Bad score..out of range')
    sys.exit()

if (score < 0.0 or score > 1.0) : print('Bad score')
elif score >= 0.9 : print('A')
elif score >= 0.8 : print('B')
elif score >= 0.7 : print('C')
elif score >= 0.6 : print('D')
elif score < 0.6 : print('F')
