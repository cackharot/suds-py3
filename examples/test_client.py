import sys
import os
suds_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(suds_path)

from suds.client import Client

def set_log():
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    logging.getLogger('suds.transport').setLevel(logging.DEBUG)

def call_service(url):
    # set_log()
    client = Client(url, username='bob', password='catbob')

    print("Calling: sayHello()")
    result = client.service.sayHello('Username')

    print("Result: %s" % result)
    a = 10.98
    b = 98.83
    print("Calling: add()")
    sum = client.service.add(a, b)
    print("Result: Sum of %f + %f = %f" % (a,b,sum))

    print("Calling: addDate()")
    from datetime import datetime
    import time
    inputDate = datetime.now()
    dt = client.service.addDate(inputDate, 1)
    print("Result: %s" % dt)

def test(url):
    client = Client(url)
    for p in client.sd[0].ports:
        for m, args in p[1]:
            if len(args) == 0:
                print(client.service[0][m]())

if __name__ == '__main__':
    url = 'http://localhost:8181/soap/helloservice?wsdl'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    call_service(url)
    # test('http://dati.meteotrentino.it/service.asmx?WSDL')
