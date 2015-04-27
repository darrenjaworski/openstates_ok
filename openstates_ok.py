from sunlight import openstates
import csv
import re

oklahoma_lower_bills = openstates.bills(
    state='ok',
    chamber='lower',
    search_window='session'
)

with open('votes.csv', 'wb') as f:
    writer = csv.writer(f)

    for bill in oklahoma_lower_bills:

        oklahoma_bill_details = openstates.bill_detail(
            state='ok',
            session='2015-2016',
            bill_id=bill['bill_id']
        )

        vote = [
            bill['bill_id'],
            oklahoma_bill_details['votes']
        ]

        for bill_votes in oklahoma_bill_details['votes']:

            pattern = re.compile('third', re.IGNORECASE)
            if pattern.match(bill_votes['motion']):
                print pattern.match(bill_votes['motion'])
            else:
                print "no match"

        #writer.writerow(vote)
