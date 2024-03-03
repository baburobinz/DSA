from eg1 import Queue
import time
import threading

order_list = Queue()

def place_order(items):    
    for item in items:
        print(f'Placing order of : {item}')
        order_list.enqueue(item)
        time.sleep(0.5)

def serve_order(orders):
    time.sleep(1)
    while orders.size()!=0:
        print(f'Served : {orders.dequeue()}')
        time.sleep(2)
        
orders = ['pizza','samosa','pasta','biryani','burger']
# place_order(orders)
# serve_order(order_list)
t1 = threading.Thread(target=place_order,args=(orders,))
t2 = threading.Thread(target=serve_order,args=(order_list,))
t1.start()
t2.start()







