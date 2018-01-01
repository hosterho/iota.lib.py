from iota import Iota
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def change_char(seed_to_change, pos, new_char):
    s = list(seed_to_change)
    s[pos] = new_char
    return "".join(s)


def perform_api_request(seed_to_get):
    api = Iota('http://5.9.149.169:14265', seed_to_get)
    return api.get_account_data(stop=1)


def check_account_info(response, seed_to_check):
    if response['balance'] is not 0 or len(response['bundles']) is not 0:
        print("Start----------------------------------")
        print("Seed: ", seed_to_check)
        print("Balance: ", response['balance'])
        print("Addresses: ", response['addresses'])
        print("Bundles: ", response['bundles'])
        print("End------------------------------------")


counter = 0
seeds = [line.rstrip('\n') for line in open('/Users/haos/PycharmProjects/SeedGrafter/seeds/in-progress/test-1')]
for seed in seeds:
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', '9']
    orig_seed = seed
    for character in characters:
        seed = change_char(seed_to_change=seed, pos=0, new_char=character)
        print("Seed No.: ", counter, "Seed: ", seed)
        api_response = perform_api_request(seed_to_get=seed)
        check_account_info(response=api_response, seed_to_check=seed)
        counter = counter + 1
        seed = orig_seed
