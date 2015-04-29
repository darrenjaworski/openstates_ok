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

# oklahoma legislators
ok_legislators = openstates.legislators(
    state='ok',
    active='true'
)

# we need an array of the legislators ids
ok_legislators_array = []
for legislator in ok_legislators:
    ok_legislators_array.append(legislator['leg_id'])

# create or open votes.csv file, with read/write
with open('votes.csv', 'w') as f:
    # create writer object on the file we named f
    # extrasaction parameter means that if there is a missing or extra leg_id in our array
    # then the writer will continue regardless
    writer = csv.DictWriter(f, fieldnames=ok_legislators_array, extrasaction='ignore')

    # write our header row with the legislators ids
    writer.writeheader()

    # loop through the bills from the previous api call
    for bill in oklahoma_lower_bills:

        # get individual details on the bills, i.e. votes
        # see example output: http://sunlightlabs.github.io/openstates-api/bills.html#examples/bill-detail
        oklahoma_bill_details = openstates.bill_detail(
            state='ok',
            session='2015-2016',
            bill_id=bill['bill_id']
        )

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
                    total_votes[yes_votes['leg_id']] = 1

                # no votes will be labeled 2
                for no_votes in bill_votes['no_votes']:
                    total_votes[no_votes['leg_id']] = 2

            # not third reading
            else:
                print "Not third reading."

            # lets try to write the total_votes using a DictWriter
            # this should let us match the specific columns to the specific voters
            try:
                writer.writerow(total_votes)
            # catch exception and print in console.
            except ValueError:
                print "Something is off in writing your csv"
