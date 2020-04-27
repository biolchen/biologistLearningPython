import time
def countdown(t):
    real = t
    while t > 0:
        CURSOR_UP = '\033[F'
        ERASE_LINE = '\033[K'
        if t == real:
            print(ERASE_LINE + 'Duration : {}s'.format(t))
        else:
            print(CURSOR_UP + ERASE_LINE + 'Duration : {}s'.format(t))
        time.sleep(1)
        t -= 1

countdown(4)