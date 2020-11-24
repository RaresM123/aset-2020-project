import requests
from aspectlib import contrib
from profilestats import profilestats
import aspectlib


@profilestats.profile(print_stats=10, dump_stats=True)
def sendSentence():
    url = r"http://127.0.0.1:5000/check_statement"
    data = {"sentence": "ana are mere"}
    r = requests.post(url, json=data, headers={'AuthorizationToken': 'xy124zjw3'})
    print(r.text)


aspectlib.weave(sendSentence, contrib.retry())

if __name__ == '__main__':
    sendSentence()