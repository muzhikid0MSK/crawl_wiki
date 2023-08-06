from threading import Lock


# thread safe counter class
class ThreadSafeCounter():
    # constructor
    def __init__(self):
        # initialize counter
        self._counter = 0
        # initialize lock
        self._lock = Lock()

    # increment the counter
    def increment(self):
        with self._lock:
            self._counter += 1

    # get the counter value
    def value(self):
        with self._lock:
            return self._counter


# thread safe counter class
class ThreadSafeLoopCounter():
    # constructor
    def __init__(self, top, bot=0, initial=0):
        # initialize counter
        self._counter = initial
        # initialize lock
        self._lock = Lock()
        self._top = top
        self._bot = bot

    # increment the counter
    def increment(self):
        with self._lock:
            self._counter += 1
            if self._counter >= self._top:
                self._counter = self._bot

    def increase_and_get(self):
        with self._lock:
            self._counter += 1
            if self._counter >= self._top:
                self._counter = self._bot
            return self._counter

    # get the counter value
    @property
    def value(self):
        with self._lock:
            return self._counter
