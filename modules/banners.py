# Import necessary modules from the os library
from os import system, name as nm

# Define a function to export data to a file
def export():
    # Call the init_banner function to display an initial banner
    init_banner()
    # Call the separator function to create a separator line in red
    separator("red")
    # Print a message with yellow color
    print(colorize_text("\n                          FILE OUTPUT", "yellow"))
    # Call the separator function to create another separator line in red
    separator("red")
    # Prompt the user for a filename and add a ".txt" extension
    file_name = str(input(colorize_text("\n[-] Insert the output file name (without extension): ", "yellow")))
    file_name = file_name + ".txt"
    # Return the constructed filename
    return file_name

# Define a function to colorize text with ANSI escape codes
def colorize_text(text, color, format=None):
    color = color.lower()
    if format != None:
        format = format.lower()

    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'new': '\033[1m',
        'reset': '\033[0m'
    }

    formats = {
        'bold': '\033[1m',
        'faint': '\033[2m',
        'italic': '\033[3m',
        'blink': '\033[5m',
    }

    if format != None:
        if color in colors:
            if format in formats:
                return f"{colors[color]}{formats[format]}{text}{colors['reset']}"
            else:
                return text
    elif format == None:
        if color in colors:
            return f"{colors[color]}{text}{colors['reset']}"
        else:
            return text
    else:
        return text

# Define a function to determine the OS command for clearing the screen
def os_id():
    if nm == "posix":
        return "clear"
    else:
        return "cls"

# Define a function to clear the screen using the appropriate OS command
def clear_screen():
    system(os_id())

# Define a function to initialize the banner
def init_banner():
    # Clear the screen
    clear_screen()
    # Call the separator function to create a separator line in cyan
    separator("cyan")
    # Call the main_banner function to display a main banner
    main_banner()
    # Call the separator function to create another separator line in cyan
    separator("cyan")

# Define a function to display the main banner
def main_banner():
    banner = """
    ███████╗██╗  ██╗███████╗██╗     ██╗     ███████╗ ██████╗ ██████╗  ██████╗ ███████╗
    ██╔════╝██║  ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
    ███████╗███████║█████╗  ██║     ██║     █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
    ╚════██║██╔══██║██╔══╝  ██║     ██║     ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
    ███████║██║  ██║███████╗███████╗███████╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ 
        
                                       V1.0

                                BY TOMAS ILLUMINATI

                     FROM REV SHELL BY RYAN MONTGOMERY (0dayCTF)
    """
    # Print the banner with green color
    print(colorize_text(banner, "green"))
    # Print a message in red
    print(colorize_text("          (This tool was created for educational and ethical use only.)   ", "red"))

# Define a function to create a separator line with a specified color
def separator(color):
    # Print a separator line with the given color
    print(colorize_text("\n--------------------------------------------------------------------------------------", color))

# Define a function to handle errors
def error(error_n):
    if error_n == 0:
        separator("red")
        print(colorize_text("\n                      [!] You need to insert an IP address","red"))
        separator("red")
    elif error_n == 1:
        separator("red")
        print(colorize_text("\n                      [!] You need to insert a number (max 65535) ","red"))
        separator("red")
    elif error_n == 2:
        separator("red")
        print(colorize_text("\n                      [!] You need to insert a number","red"))
        separator("red")

# Define a function to display a list of reverse shell formats
def lang_list():
    # Display a list of reverse shell formats with options
    print(colorize_text("\nSELECT THE REVERSE SHELL FORMAT: ", "red", "bold"))


    print(colorize_text("\n[1] Awk", "yellow"))
    print(colorize_text("\n[2] Bash -i", "yellow"))
    print(colorize_text("\n[3] Bash 5", "yellow"))
    print(colorize_text("\n[4] Bash 196", "yellow"))
    print(colorize_text("\n[5] Bash read line", "yellow"))
    print(colorize_text("\n[6] Bash udp", "yellow"))
    print(colorize_text("\n[7] BusyBox nc -e", "yellow"))
    print(colorize_text("\n[8] C# TCP Client", "yellow"))
    print(colorize_text("\n[9] C# Bash -i", "yellow"))
    print(colorize_text("\n[10] C", "yellow"))
    print(colorize_text("\n[11] C Windows", "yellow"))
    print(colorize_text("\n[12] Crystal (code)", "yellow"))
    print(colorize_text("\n[13] Crystal (system)", "yellow"))
    print(colorize_text("\n[14] curl", "yellow"))
    print(colorize_text("\n[15] Dart", "yellow"))
    print(colorize_text("\n[16] Groovy", "yellow"))
    print(colorize_text("\n[17] Golang", "yellow"))
    print(colorize_text("\n[18] Heskell", "yellow"))
    print(colorize_text("\n[19] Java #1", "yellow"))
    print(colorize_text("\n[20] Java #2", "yellow"))
    print(colorize_text("\n[21] Java #3", "yellow"))
    print(colorize_text("\n[22] Java Web", "yellow"))
    print(colorize_text("\n[23] Java Two Way", "yellow"))
    print(colorize_text("\n[24] Javascript", "yellow"))
    print(colorize_text("\n[25] Lua #1", "yellow"))
    print(colorize_text("\n[26] Lua #2", "yellow"))
    print(colorize_text("\n[27] nc -c", "yellow"))
    print(colorize_text("\n[28] nc -e", "yellow"))
    print(colorize_text("\n[29] nc mkfifo", "yellow"))
    print(colorize_text("\n[30] nc.exe -e", "yellow"))
    print(colorize_text("\n[31] ncat.exe -e", "yellow"))
    print(colorize_text("\n[32] ncat udp", "yellow"))   
    print(colorize_text("\n[33] node.js #1", "yellow"))
    print(colorize_text("\n[34] node.js #2", "yellow"))
    print(colorize_text("\n[35] Perl", "yellow"))
    print(colorize_text("\n[36] Perl no sh", "yellow"))
    print(colorize_text("\n[37] PHP cmd", "yellow"))
    print(colorize_text("\n[38] PHP cmd #2", "yellow"))
    print(colorize_text("\n[39] PHP cmd Small", "yellow"))
    print(colorize_text("\n[40] PHP exec", "yellow"))
    print(colorize_text("\n[41] PHP passthru", "yellow"))
    print(colorize_text("\n[42] PHP popen", "yellow"))
    print(colorize_text("\n[43] PHP proc_open", "yellow"))
    print(colorize_text("\n[44] PHP shell_exec", "yellow"))
    print(colorize_text("\n[45] PowerShell #1", "yellow"))
    print(colorize_text("\n[46] PowerShell #2", "yellow"))
    print(colorize_text("\n[47] PowerShell #3", "yellow"))
    print(colorize_text("\n[48] PowerShell #4 (TLS)", "yellow"))
    print(colorize_text("\n[49] Python #1", "yellow"))
    print(colorize_text("\n[50] Python #2", "yellow"))
    print(colorize_text("\n[51] Python3 #1", "yellow"))
    print(colorize_text("\n[52] Python3 #2", "yellow"))
    print(colorize_text("\n[53] Python3 shortest", "yellow"))
    print(colorize_text("\n[54] Python3 Windows", "yellow"))
    print(colorize_text("\n[55] Ruby", "yellow"))
    print(colorize_text("\n[56] Ruby no sh", "yellow"))
    print(colorize_text("\n[57] rustcat", "yellow"))
    print(colorize_text("\n[58] socat #1", "yellow"))
    print(colorize_text("\n[59] socat #2 (TTY)", "yellow"))
    print(colorize_text("\n[60] sqlite3 nc mkfifo", "yellow"))
    print(colorize_text("\n[61] telnet", "yellow"))
    print(colorize_text("\n[62] Vlang", "yellow")) 
    print(colorize_text("\n[63] zsh", "yellow"))
    # Prompt the user for their selection
    answer = input(colorize_text("\n[-] Your Selection: ", "cyan"))
    return answer

# Define a function to handle restart errors
def restart_error():
    separator("red")
    print(colorize_text("\n                [!] The Answer must be (Y) or (N)", "red"))
    separator("red")
