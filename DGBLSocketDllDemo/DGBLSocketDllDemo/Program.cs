using System;
using System.Runtime.InteropServices;
using System.Text;

namespace DGBLSocketDllDemo
{
    class EchoClient
    {
        EchoClient(string addr, string port) {
            byte[] baddr = Encoding.ASCII.GetBytes(addr),
                bport = Encoding.ASCII.GetBytes(port);
            unsafe
            {
                fixed (byte* a = baddr, p = bport)
                {
                    sbyte* sp = (sbyte*)p, sa = (sbyte*)a;
                    clr = new ClrClass(sa, sp);
                }
            }
        }

        ~EchoClient()
        {
            clr.close();
        }

        string RecvMsg() {
            int ret = clr.recvMessage();
            if (ret > 0) {
                byte[] bytes = new byte[ret];
                unsafe
                {
                    for (int i = 0; i < ret; i++) {
                        bytes[i] = (byte)*(clr.recvBuf + i);
                    }
                }
                return Encoding.Default.GetString(bytes);
            }
            return null;
        }

        void sendMsg(string str) {
            byte[] bytes = Encoding.ASCII.GetBytes(str);
            int num = Encoding.ASCII.GetByteCount(str);
            unsafe
            {
                fixed (byte* b = bytes)
                {
                    sbyte* sb = (sbyte*)b;
                    clr.sendMessage(sb, num);
                }
            }
        }

        public ClrClass clr;

        static void Main(string[] args)
        {
            Console.WriteLine("Hello world");
            EchoClient client = new EchoClient("127.0.0.1", "8002");
            client.sendMsg("Hello");
            string recv = null;
            while (recv == null) {
                recv = client.RecvMsg();
            }
            Console.WriteLine(recv);
        }
    }
}
