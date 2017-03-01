import time


class Message(object):
    def __init__(self, message):
        """
        Args:
           message (str): message string
        """
        self.message = message
        self.timestamp = time.time()

        
class MessageCounter(object):
    def __init__(self, match_string, duration=10, debug=False):
        """
        Args:
           match_string (str): message string to be matched.
           duration (float): number of matching messages within this 
                  duration(in seconds) is counted.
           debug (bool): If True debug info will be printed out
        """
        self.duration  = duration
        self.match_string = match_string
        self.debug = debug
        self.cache = []

    def __call__(self, msg):
        """
        Args:
           msg (Message): incoming Message object.

        Returns:
           int: number of matching messages within the given duration.
        """        
        now = time.time()
        remove_indices = []
        if self.debug:
            print(now)
        if msg.message == self.match_string:
           self.cache.append(msg)
        for i, msgi in enumerate(self.cache):
           if now - msgi.timestamp > self.duration:
               remove_indices.append(i)
        remove_indices.reverse()
        for i in remove_indices:
            del self.cache[i]
        return len(self.cache)
