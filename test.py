import time
import unittest

from message_counter import Message, MessageCounter


class MessageCounterTest(unittest.TestCase):
    
    def setUp(self):
        self.match_string = "tr_test"
        self.msg_counter = MessageCounter(self.match_string, duration=10)
        
    def test_counter(self):
        test_msgs = []
        for i in range(4):
            time.sleep(1)
            msg = Message(self.match_string)
            test_msgs.append(msg)
        for i in range(4):
            time.sleep(1)
            msg = Message("some_non-matching_string")
            test_msgs.append(msg)
        for i in range(7):
            time.sleep(1)
            msg = Message(self.match_string)
            test_msgs.append(msg)
        
        count = 0
        
        for msg in test_msgs:
            count=self.msg_counter(msg)
            
        self.assertEqual(count, 7)
