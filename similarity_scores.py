# This script will read the data from openstates_ok.py
# and create a similarity score for each legislator to
# one another.

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

with open('scores.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=ok_legislators_array, extrasaction='ignore')
    writer.writeheader()

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

                leg_scores = {}

                try:
                    score = float(voteSame) / voteCount
                    leg_scores[legislatorB] = score

                except ZeroDivisionError:
                    print "No votes were comparable."
                    leg_scores[legislatorB] = "x"

            try:
                writer.writerow(leg_scores)
                print "wrote something"
            except ValueError:
                print "blew up"
