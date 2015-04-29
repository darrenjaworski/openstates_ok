# import packages we need: openstates, csv, and regex
from sunlight import openstates
import csv
import re

# api call using openstates package.
# see example output: http://sunlightlabs.github.io/openstates-api/bills.html#examples/bill-search
oklahoma_lower_bills = openstates.bills(
    state='ok',
    chamber='lower',
    search_window='session'
)

# create or open votes.csv file, with read/write
with open('votes.csv', 'wb') as f:
    # create writer object on the file we named f
    writer = csv.writer(f)

    # loop through the bills from the previous api call
    for bill in oklahoma_lower_bills:

        # get individual details on the bills, i.e. votes
        # see example output: http://sunlightlabs.github.io/openstates-api/bills.html#examples/bill-detail
        oklahoma_bill_details = openstates.bill_detail(
            state='ok',
            session='2015-2016',
            bill_id=bill['bill_id']
        )

        # create vote array for a row on our csv
        vote = [
            bill['bill_id'],
            oklahoma_bill_details['votes']
        ]

        # loop through votes looking for the third reading
        for bill_votes in oklahoma_bill_details['votes']:

            # we're looking for 'third' either upper or lower case (upper in this instance, but might be odd ball)
            pattern = re.compile('third', re.IGNORECASE)

            # if the motion matches 'third'
            if pattern.match(bill_votes['motion']):

                total_votes = {}

                # other votes will be nominally labeled 3
                for other_votes in bill_votes['other_votes']:
                    total_votes[other_votes['leg_id']] = 3

                # yes votes will be labeled 1
                for yes_votes in bill_votes['yes_votes']:
                    total_votes[other_votes['leg_id']] = 1

                # no votes will be labeled 2
                for no_votes in bill_votes['no_votes']:
                    total_votes[other_votes['leg_id']] = 2

            # not third reading
            else:
                print "Not third reading."

        # this part isn't ready yet, but we'll organize the data and write it to a csv file.
        #writer.writerow(vote)
