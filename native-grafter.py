from iota import Iota
import sys
reload(sys)
sys.setdefaultencoding('utf8')

counter = 0
seeds = [line.rstrip('\n') for line in open('/Users/haos/PycharmProjects/SeedGrafter/seeds/in-progress/some-working-seeds-to-test')]
for seed in seeds:
    if (counter % 100) == 0:
        print("Seed No.: ", counter)
    counter = counter + 1
    print('Seed No.: ' + str(counter) + '  -  Seed: ' + str(seed))
    api = Iota('http://5.9.149.169:14265', seed)
    api_response = api.get_account_data(stop=1)
    if api_response['balance'] is not 0 or len(api_response['bundles']) is not 0:
        print('is working')
        textFile = open('/Users/haos/PycharmProjects/SeedGrafter/seeds/working_seeds/seeds-1', 'a')
        textFile.write('Seed: ' + str(seed) + '\n')
        textFile.write('Balance: ' + str(api_response['balance']) + '\n')
        textFile.write('Addresses: ' + str(api_response['addresses']) + '\n')
        textFile.write('Bundles: ' + str(api_response['bundles']) + '\n')
        textFile.write('\n')
        textFile.write('\n')
        textFile.close()
