from sunlight import openstates

oklahoma_lower_bills = openstates.bills(
    state='ok',
    chamber='lower',
    search_window='session'
)

votes = []

for bill in oklahoma_lower_bills:

    oklahoma_bill_details = openstates.bill_detail(
        state='ok',
        session='2015-2016',
        bill_id=bill['bill_id']
    )

    vote = {}
    vote['bill_id'] = bill['bill_id']
    vote['votes'] = oklahoma_bill_details['votes']

    votes.append(vote)

    print votes
