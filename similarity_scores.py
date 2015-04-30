# This script will read the data from openstates_ok.py
# and create a similarity score for each legislator to
# one another.

# for legislator in legislators
    # compare legislator 1 to every other by bill votes
    # for legislator in legislators

        # for bill in bills
            # generate score based on similarity of voting

        # store score for legislator 1 to another legislator

    # write scores into a single row

import csv
from sunlight import openstates

ok_legislators = openstates.legislators(
    state='ok',
    active='true'
)

# ok_legislators_array = ['legi_id']
ok_legislators_array = []
for legislator in ok_legislators:
    ok_legislators_array.append(legislator['leg_id'])

for legislatorA in ok_legislators_array:
    print "Going through " + legislatorA

    for legislatorB in ok_legislators_array:
        print "Comparing " + legislatorA + " to " + legislatorB

        with open('votes.csv') as f:
            reader = csv.DictReader(f)

            voteCount = 0
            voteSame = 0
            notComparable = 0

            for bill in reader:
                if not bill[legislatorA] or not bill[legislatorB]:
                    notComparable += 1
                    #print "not comparable"
                elif bill[legislatorA] == bill[legislatorB]:
                    voteCount += 1
                    voteSame += 1
                    #print "same vote"
                else:
                    voteCount += 1
                    #print "different vote"
