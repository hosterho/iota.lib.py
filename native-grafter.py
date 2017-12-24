from iota import Iota
import sys
reload(sys)
sys.setdefaultencoding('utf8')

counter = 0
seeds = [line.rstrip('\n') for line in open('/Users/haos/PycharmProjects/SeedGrafter/seeds/in-progress/test-1')]
for seed in seeds:
    if (counter % 100) == 0:
        print("Seed No.: ", counter)
    counter = counter + 1
    api = Iota('http://5.9.149.169:14265', seed)
    api_response = api.get_account_data(stop=1)
    if api_response['balance'] is not 0 or len(api_response['bundles']) is not 0:
        print("Start----------------------------------")
        print("Seed: ", seed)
        print("Balance: ", api_response['balance'])
        print("Addresses: ", api_response['addresses'])
        print("Bundles: ", api_response['bundles'])
        print("End------------------------------------")
