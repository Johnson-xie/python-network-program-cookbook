#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create Time: 9/9/2015 4:07p
# ˵���������ֽ���������ֽ�����໥ת��

import socket

def convert_integer():
	data=1234
	# 32bit
	print "Original: %s => Long host byte order: %s Network byte order: %s"\
		%(data,socket.ntohl(data),socket.htonl(data))
	#16bit
	print "Originall: %s => Short host byte order: %s Network byte order: %s"\
		%(data,socket.ntohs(data),socket.htons(data))
	
if __name__=='__main__':	
	convert_integer()
