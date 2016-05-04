import os

redis_host = os.getenv('REDIS_HOST', 'localhost:6379')

REDIS = dict(
        host=redis_host.split(':')[0],
        port=redis_host.split(':')[1],
        db='0',
        password=os.getenv('REDIS_PASSWORD', None),
        socket_timeout=2,
        socket_connect_timeout=2,
        )

