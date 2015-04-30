# This script will read the data from openstates_ok.py
# and create a similarity score for each legislator to
# one another.

import csv
from sunlight import openstates

# get list of legislators
ok_legislators = openstates.legislators(
    state='ok',
    active='true'
)

# redundant, but I'm using a DictWriter key
# and one array to use in loops
ok_legislators_csv_key = ['leg_id']
ok_legislators_array = []
for legislator in ok_legislators:
    ok_legislators_csv_key.append(legislator['leg_id'])
    ok_legislators_array.append(legislator['leg_id'])

# new csv file that we're going to write our matrix of values to
with open('scores.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=ok_legislators_csv_key, extrasaction='ignore')
    writer.writeheader()

    # first loop of legislators
    for legislatorA in ok_legislators_array:
        print "Going through " + legislatorA

        # our dictionary for each row
        # we add the first column label
        leg_scores = {}
        leg_scores['leg_id'] = legislatorA

        # second loop of legislators so we can
        # compare one legislator to another
        for legislatorB in ok_legislators_array:

            # open the votes csv file
            with open('votes.csv') as f:
                reader = csv.DictReader(f)

                # these variables are to calculate our similarity scores
                voteCount = 0
                voteSame = 0
                notComparable = 0

                # since we opened the votes file
                # each row in the file represents a bill
                for bill in reader:

                    # comparing the votes to calculate similarity score
                    if not bill[legislatorA] or not bill[legislatorB]:

                        notComparable += 1

                    elif bill[legislatorA] == bill[legislatorB]:

                        voteCount += 1
                        voteSame += 1

                    else:

                        voteCount += 1

                # I noticed some of the legislators aren't voting on all the bills together,
                # probably because there is a mix of upper and lower house members.
                # So we catch any exception with no voteCount, meaning a division by zero.
                try:
                    score = float(voteSame) / voteCount
                    leg_scores[legislatorB] = score

                except ZeroDivisionError:
                    leg_scores[legislatorB] = "x"

        # write a row for one legislator into the csv
        # with similarity scores amongst all other legislators
        writer.writerow(leg_scores)
