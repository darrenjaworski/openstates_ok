import urllib2, json

API_KEY = '70f72edb0e034b10bc328c468e591b54'

def get_bills(state, chamber):

    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=%s&session=2015-2016&chamber=%s&type=bill&apikey=%s' % (state, chamber, API_KEY))
    json_object = json.load(response)

    for result in json_object:
        print result['bill_id']

    return

get_bills('ok', 'lower')
