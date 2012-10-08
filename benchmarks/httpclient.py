import time
import gevent.pool
from geventhttpclient import HTTPClient, URL
from urlname import *
import redis
import cPickle as pickle


if __name__ == "__main__":

    N = 10000
    C = 200

    r = redis.Redis()

    urls = [URL(url) for url in all_url]

    def run(num):
        try:
            response = clients[num].get(urls[num].request_uri)
            result=response.read()
            p = pickle.dumps(result)
            r.lpush("htmlbase",p)
            assert response.status_code == 200
        except :
            print "time out"


    clients = [HTTPClient.from_url(url, concurrency=C,connection_timeout=10,network_timeout=10) for url in urls]
    group = gevent.pool.Pool(size=C)

    now = time.time()
    for i in xrange(N):
        group.spawn(run, i%8)
        print i
    group.join()

    delta = time.time() - now
    req_per_sec = N / delta

    print "request count:%d, concurrenry:%d, %f req/s" % (
    N, C, req_per_sec)


