from threading import Timer
def hello():
    print("Hello World!")


class RepeatingTimer(object):

    def __init__(self, interval, f, *args, **kwargs):
        self.interval = interval
        self.f = f
        self.args = args
        self.kwargs = kwargs
        self.timer = None
        self.status = False

    def callback(self):
        self.f(*self.args, **self.kwargs)
        self.status = False
        #self.timer.cancel()

    def cancel(self):
        self.status = False
        self.timer.cancel()
        

    def start(self):
        self.status = True
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()

t = RepeatingTimer(3, hello)
t.start()

