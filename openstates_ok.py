from sunlight import openstates

oklahoma_bills = openstates.bills(
    state='ok',
    chamber='lower'
)

for bill in oklahoma_bills:
    print bill['title']
