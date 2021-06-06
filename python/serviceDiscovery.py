import nacos
import sys
from nacos.listener import SubscribeListener, SimpleListenerManager
from nacos.timer import NacosTimer, NacosTimerManager

SERVER_ADDRESSES = "127.0.0.1:8848"
NAMESPACE = ""

# Set the following values if authentication mode is enabled on the server
USERNAME = None
PASSWORD = None

client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username=USERNAME, password=PASSWORD)

client.set_debugging()

flag = client.add_naming_instance("python", "127.0.0.1", 9999, "", 1, "{}", True, True)

print('服务注册成功')

def heartbeat(self):
    client.send_heartbeat("python", "127.0.0.1", 9999, "", 1, "{}")["clientBeatInterval"]
    pass


nt1 = NacosTimer("test_timer1", heartbeat, 5, "nacos1")
ntm = NacosTimerManager()
ntm.add_timer(nt1)
ntm.execute()

def fn_listener1(event, instance):
    print("fn_listener1 is listening ==> ", event, instance.instance)
    pass


fn1 = SubscribeListener(fn=fn_listener1, listener_name="fn_listener1")
client.subscribe(fn1, 7, "python")
print("subscribe finished")