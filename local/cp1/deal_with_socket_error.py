#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create Time: 9/9/2015 4:26p
# ˵����ִ�� python THIS_FILE.py --host=www.qq.com --port=80
# ���󣺷���400���󣬻���һ����Ϣ
# ����socket�������ӷ��������������ݣ��ȴ�Ӧ��

import sys
import socket
import argparse

def main():
	#�����βεļ��
	parser=argparse.ArgumentParser(description='Socket Errot Examples')
	parser.add_argument('--host',action="store",dest="host",required=False)
	parser.add_argument('--port',action="store",dest="port",type=int,required=False)

	given_args=parser.parse_args()
	host=given_args.host
	port=given_args.port


	#����socket
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except socket.error,e:
		print "error creating socket!%s"%e
		sys.exit(1)
	#����socket 
	try: 
		s.connect((host,port))
	except socket.gaierror,e:
		print "error Address-related error connecting to server: %s"%e
		sys.exit(1)
	except socket.error,e:
		print "error connection!%s"%e
		sys.exit(1)
	#�������� 
	try: 
		s.sendall("GET HTTP/1.0\r\n\r\n")
	except socket.error,e: 
		print "error sending data: %s"%e
		sys.exit(1);
	#��������  
	while 1: 
		try:
			buf=s.recv(2048)
		except socket.error,e:  
			print "error recieving data: %s"%e
			sys.exit(1)
		if not len(buf): 
			break
			#д������ 
		sys.stdout.write(buf)
	  
if __name__=='__main__': 
	main()   
