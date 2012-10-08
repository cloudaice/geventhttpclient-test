import redis
import cPickle as pickle

r = redis.Redis()

count =0 ;
t =  r.rpop("htmlbase")
while t:
    data = pickle.loads(t)
    count = count + 1
    t = r.rpop("htmlbase")

print count
