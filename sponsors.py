# spreadsheet for all the bills sponsored by legislator

from sunlight import openstates
import csv

oklahoma_bills = openstates.bills(
    state='ok',
    search_window='term:2015-2016'
)

ok_sponsors = ['bill_id', 'sponsor_1', 'sponsor_2']

with open('sponsored.csv', 'w') as f:

    writer = csv.DictWriter(f, fieldnames=ok_sponsors, extrasaction='ignore')
    writer.writeheader()
    loop = 0

    for bill in oklahoma_bills:

        oklahoma_bill_details = openstates.bill_detail(
            state='ok',
            session='2015-2016',
            bill_id=bill['bill_id']
        )

        row = {}
        row['bill_id'] = oklahoma_bill_details['id']
        row['sponsor_1'] = oklahoma_bill_details['sponsors'][0]['leg_id']
        if len(oklahoma_bill_details['sponsors']) > 1:
            row['sponsor_2'] = oklahoma_bill_details['sponsors'][1]['leg_id']
        else:
            row['sponsor_2'] = ''

        writer.writerow(row)

        loop += 1

        print "%s of %d" %(loop, len(oklahoma_bills))
