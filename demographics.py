from sunlight import openstates
import csv

ok_legislators = openstates.legislators(
    state='ok',
    active='true'
)

with open('demographics.csv', 'w') as f:

    fieldNames = ['leg_id', 'first_name', 'last_name', 'chamber', 'party', 'district']
    writer = csv.DictWriter(f, fieldnames=fieldNames, extrasaction='ignore')
    writer.writeheader()

    for legislator in ok_legislators:

        info = {}
        info['leg_id'] = legislator['id']
        info['first_name'] = legislator['first_name']
        info['last_name'] = legislator['last_name']
        info['chamber'] = legislator['chamber']
        info['party'] = legislator['party']
        info['district'] = legislator['district']

        writer.writerow(info)
