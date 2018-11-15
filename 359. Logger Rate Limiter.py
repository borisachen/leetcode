359. Logger Rate Limiter

Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), 
return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

-----
Use a dictionary to track all the messages.
key = message, value = timestamp
if a new message is not in the dict, then we add it and return true.
if a new message is in the dict, and it has expired, then we refresh the ts and return true.
-----

class logger(object):
	def __init__(self):
		self.m = {}
	def shouldPrintMessage(self, msg, ts):
		if msg not in m:
			m[msg] = ts
			return True
		if ts - m[msg] >= 10:
			m[msg] = ts
			return True
		return False
