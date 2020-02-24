# Data analysis
Reviews on Amazon Echo, Google Home and Apple HomePod



### Redis

Install **[redis](https://redis.io/topics/quickstart)**

Start Redis under its path, e.g. `/Users/allen/redis-stable`
> src/redis-server redis.conf

Shut down server
> redis-cli shutdown

### Setup proxypool

> cd proxy/proxypool

In the folder of `proxypool`, vim file `settings.py` , setup the `PASSWORD` which is Redis password; if no password, leave it `None`
>  REDIS_PASSWORD = None

### Run proxy and API

> python3 proxy/run.py

#### Get the IP
In the file `proxy_list.py`
Get the ip and random list or from redis.