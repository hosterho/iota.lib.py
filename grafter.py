from iota import Iota
from six import binary_type
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

counter = 0
seeds = [line.rstrip('\n') for line in open('/Users/haos/PycharmProjects/SeedGrafter/seeds/0-200-pseudo-random-seeds')]
for seed in seeds:
    print("Seed No.: ", counter)
    counter = counter + 1
    url_prefix = "https://iotasear.ch/hash/"
    api = Iota("http://5.9.149.169:14265", seed)
    api_response = api.get_new_addresses(index=0, count=1)
    for addy in api_response['addresses']:
        address_string = binary_type(addy).decode('utf8')
        url = url_prefix + address_string
        r = requests.get(url)
        if address_string in r.content:
            print("Seed", seed)
            print("exists")
            print(r.content)
            if " Ki</div" or " Mi</div" or " Gi</div" or " Ti</div" in r.content:
                print("There was activity in Balance")
            else:
                print("no Balance")
