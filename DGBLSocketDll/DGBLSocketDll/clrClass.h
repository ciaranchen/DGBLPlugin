#pragma once

#undef UNICODE
#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>
#pragma comment(lib,"ws2_32.lib")

#define RECVBUFLEN 1024

public ref class ClrClass
{
public:
	// create socket
	ClrClass(char[], char[]);

	// send message
	int sendMessage(char[], int);

	// recv message
	int recvMessage();

	// close link
	void close();

	// for test
	int test() {
		return 233;
	}

	char* recvBuf;
	int err_code = 0;
private:
	SOCKET ConnectSocket;
};