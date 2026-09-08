def outer(fun):
    def inner():
        print("I will sleep")
        fun()
        print("I get up")
    return inner

@outer
def sleep():
    import time
    import random
    print("sleeping....")
    time.sleep(random.randint(1,5))


sleep()