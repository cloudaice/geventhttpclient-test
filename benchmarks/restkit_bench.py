if __name__ == "__main__":


    from urlname import *
    from gevent import monkey
    monkey.patch_all()

    import gevent.pool
    import time

    from restkit import *
    from socketpool import ConnectionPool

    #url = 'http://127.0.0.1/index.html'

    N = 5000
    C = 80

    Pool = ConnectionPool(factory=Connection,backend="gevent",max_size=C,timeout=300)


    def run(num):
        response = request(all_url[num],follow_redirect=True,pool=Pool)
        response.body_string()
        assert response.status_int == 200


    group = gevent.pool.Pool(size=C)

    now = time.time()
    for i in xrange(N):
        group.spawn(run,i%8)
        print i
    group.join()

    delta = time.time() - now
    req_per_sec = N / delta

    print "request count:%d, concurrenry:%d, %f req/s" % (
        N, C, req_per_sec)

