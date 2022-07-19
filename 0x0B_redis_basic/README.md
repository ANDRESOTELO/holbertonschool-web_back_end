# 0x0B_redis_basic
### Redis with python
We need to install redis and redis server

### Install Redis on Ubuntu 18.04
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

### Use Redis in a container
service redis-server start
