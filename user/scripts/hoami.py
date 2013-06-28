import urllib2
import urllib
import requests
import json
import orcid
import matplotlib.pyplot as plt

ORCID_BASE_URL = 'http://pub.orcid.org/'
OAG_BASE_URL = 'http://oag.cottagelabs.com/lookup/'
TEST_ID ='0000-0002-0068-716X'
TEST_DOI = '10.1371/journal.pone.0001164'
ORCID_HEADERS = {'Accept' : 'application/orcid+json'}
OAG_HEADERS = {'Accept' : 'application/json'}

def list_works(orcid_id):
    response = orcid.get(orcid_id)
    print "Getting works for:", response.given_name, response.family_name
    id_list = []
    for pub in response.publications:
        if pub.external_ids:
            i = [id.type == 'DOI' for id in pub.external_ids].index(True)
            if i is not None:
                id_list.append(pub.external_ids[i].id)
        #except TypeError:
            #pass
    return id_list


def chart(open_count, total_count):
    labels = 'Open', 'Closed'
    fracs = [open_count, total_count-open_count]
    plt.pie(fracs, labels=labels)
    
class OAG_Request:
    def __init__(self, id_list):
        self.id_list = id_list
        self.post = None
        
    def add_id(self, id):
        self.id_list.append(id)
        
    def post_list(self):
        list = json.dumps(self.id_list)
        req = urllib2.Request(OAG_BASE_URL, list, OAG_HEADERS)
        self.post = urllib2.urlopen(req)
        return self.post
        
    def get_list(self):
        url = self.build_url()
        req = urllib2.Request(url)
        req.add_header('Accept','application/json')
        self.get = urllib2.urlopen(req)
        return self.get
        
    def jsonize(self):
        self.json = json.loads(self.get.read())
        return self.json
        
        
    def build_url(self):
        url = OAG_BASE_URL + ','.join(self.id_list)
        return url  

class OAG_Response:
    def __init__(self, response):
        self.dict = response
        
    def length(self):
        return len(self.dict.get('results'))
        
    def is_open(self, work):
        if work['license'][0]['open_access']:
            return True
        else: return False
        
    def count_open(self):
        count = 0
        for work in self.dict['results']:
            if self.is_open(work):
                count += 1
            
        return count

        
if __name__ == '__main__':
    ids = list_works(TEST_ID)
    request = OAG_Request(ids)
    request.post_list()
    request.get_list()
    response = OAG_Response(request.jsonize())
    print "Total Papers:", response.length()
    print "Open Papers:", response.count_open()
    chart(response.count_open(), response.length())