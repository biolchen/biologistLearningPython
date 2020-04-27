import time
import threading

# set global variable flag
flag = 1


def message():
    global flag
    while flag == 1:
        time.sleep(1)
        print('To be, or not to be, that is the question')
        time.sleep(2)
        if not flag:
            print('End of the message \U0000203c')


def interrupt():
    global flag
    input('Press a key to stop messaging... \n')
    # thread doesn't continue until key is pressed
    flag = False
    print('flag is now:', flag)


if __name__ == '__main__':
    i = threading.Thread(target=interrupt)
    n = threading.Thread(target=message)
    n.start()
    i.start()
