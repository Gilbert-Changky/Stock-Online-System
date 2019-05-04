import socket
import sys
import threading

# import response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server created.')

host = socket.gethostbyname('localhost')
port = 9999
try:
	server.bind((host,port))
except socket.error as msg:
	print ('Bind failed. Error Code :' + str(msg))
	sys.exit()
print('Socket bind complete')

# limitated num connected to server
server.listen(5)
connectedNum = 0
print('Server now listening, limited 5, connected 0')
def result2(conn):
	conn.send('\nSignIN\n'.encode('utf-8'))
	conn.recv(1024).decode('utf-8')

def switch(head,conn):
    return {
        # '1': response.signUp(),
        # '2': response.signIn(),
        '2': result2(conn),
        # '3': response.reqData1(),
        # '4': response.reqData2(),
        # '5': response.reqData3(),
        # '6': response.reqPrefer(),
        # '7': response.addPrefer(),
        # '8': response.exit(),
    	conn.recv(1024).decode('utf-8')
    }[head]

def parseData(msg):
	head = str(msg).split('\r\n')[0]
	return head

class myThread(threading.Thread):
	def __init__(self, threadID, name, conn, ):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.conn = conn

	def run(self):
		print("Starting" + self.name)
		threadLock.acquire()
		clientThread(conn)
		threadLock.release()

def clientThread(conn):
	global connectedNum
	conn.send('hello\n'.encode('utf-8'))

	while True:
		data = conn.recv(1024).decode('utf-8')
		head = parseData(data)
		
		switch(head,conn)
		# if head == '2':
		# 	conn.send('\nTrue'.encode('utf-8'))
		# 	break
		# if data.decode('utf-8') == 'exit\r\n':
		# 	connectedNum -= 1
		# 	print('Connection %s break, connected: %d' % (str(addr), connectedNum))
		# 	self.conn.close()
		# else:
		# 	print(data)
		# 	reply = '\nreceive' + data
		# 	conn.sendall(reply.encode('utf-8'))


while True:
	conn, addr = server.accept()
	connectedNum += 1
	print('Conneced with address: %s, connected: %d' % (str(addr), connectedNum))
	msg1 = 'welcome\n'

	threadLock = threading.Lock()
	threads = []

	num = 'Thread'+str(connectedNum)
	threadCreated = myThread(connectedNum, num, conn)

	# Start new Threads
	threadCreated.start()

	# Add threads to thread list
	threads.append(threadCreated)

server.close()