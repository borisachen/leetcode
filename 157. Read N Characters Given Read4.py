157. Read N Characters Given Read4

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.

------------------------------------

initialize a temp buffer, and a counter to track the number of characters written.
use a while loop, with the exit condition being nwritten < n.


------------------------------------

def read(buf, n)
	write = 0 # number of characters written
	tempBuf = [None] * 4
	endReached = False
	while index < n:
		thisSize = read4(tempBuf)
		if thisSize < 4:
			endReached=True
		for i in range(thisSize):
			buf[write] = tempBuf[i]
			write += 1
			if write == n:
				break
	return write