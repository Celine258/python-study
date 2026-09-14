import threading,time
def sing(msg):
    while True:
        print(f"{msg},lalalala")
        time.sleep(1)

def dance(msg):
    while True:
        print(f"{msg},dadadada")
        time.sleep(1)

sing_thread = threading.Thread(target=sing,args=("I am singing",))
dance_thread = threading.Thread(target=dance,kwargs={"msg": "I am dancing"})

sing_thread.start()
dance_thread.start()