from iota import Iota
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

counter = 12170
while counter is not 2147483647:
    seed = os.popen('/usr/local/microsoft/powershell/6.0.0-rc.2/pwsh '
                    '/Users/haos/PycharmProjects/SeedGrafter/seeds/seed_generator/specific_seed.ps1 ' + str(
                     counter)).read()[:-1]
    log_string = 'Seed No.: ' + str(counter) + '  -  Seed: ' + str(seed)
    api = Iota('http://5.9.149.169:14265', seed)
    api_response = api.get_account_data(stop=1)
    if api_response['balance'] is not 0 or len(api_response['bundles']) is not 0:
        log_string = log_string + ' <-- is working'
        textFile = open('/Users/haos/PycharmProjects/SeedGrafter/seeds/working_seeds/bottom_up', 'a')
        textFile.write('Seed: ' + str(seed) + '\n')
        textFile.write('Balance: ' + str(api_response['balance']) + '\n')
        textFile.write('Addresses: ' + str(api_response['addresses']) + '\n')
        textFile.write('Bundles: ' + str(api_response['bundles']) + '\n')
        textFile.write('\n')
        textFile.write('\n')
        textFile.close()
    counter = counter + 1
    print(log_string)
