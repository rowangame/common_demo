import redis

def connect_to_redis(host, port, password):
    try:
        # 创建Redis连接对象
        redis_client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            decode_responses=True
        )
        # 测试连接
        redis_client.ping()
        print("成功连接到Redis")
        return redis_client
    except Exception as e:
        print(f"连接Redis失败: {e}")
        return None

def write_to_redis(redis_client, key, value):
    try:
        # 将数据写入Redis
        redis_client.set(key, value)
        print(f"成功写入数据: {key} = {value}")
    except Exception as e:
        print(f"写入数据失败: {e}")

def read_from_redis(redis_client, key):
    try:
        # 从Redis中读取数据
        value = redis_client.get(key)
        if value:
            print(f"读取的值: {value}")
        else:
            print(f"Key '{key}' 不存在")
    except Exception as e:
        print(f"读取数据失败: {e}")

def close_redis_connection(redis_client):
    # Redis-py使用连接池，因此无需显式关闭连接
    # 但是可以关闭连接池中的所有连接
    try:
        redis_client.connection_pool.disconnect()
        print("成功关闭Redis连接")
    except Exception as e:
        print(f"关闭Redis连接失败: {e}")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8899
    password = "123456"
    key_to_write = "key1"
    value_to_write = "value1"
    key_to_read = "key1"

    # 连接到Redis
    redis_client = connect_to_redis(host, port, password)

    if redis_client:
        # 向Redis中写入数据
        write_to_redis(redis_client, key_to_write, value_to_write)

        # 从Redis中读取数据
        read_from_redis(redis_client, key_to_read)

        # 关闭Redis连接
        close_redis_connection(redis_client)