# Import custom banners and functions modules
from modules.banners import *
from modules.functions import *
from modules.rev_shells_1 import *
from modules.rev_shells_2 import *
from modules.rev_shells_3 import *

# Function to restart the script
def restart(flag=0):
    if flag == 0:
        init_banner()
        response = str(input(colorize_text("\n[!] DO YOU WANT TO RESTART? (y/n)\n\n>>> ", "yellow")))
        response = response.lower()
        if response == "n":
            print(colorize_text("\n[!] SCRIPT FINISHED\n", "cyan"))
        elif response == "y":
            main()  # Restart the main function
        else:
            restart(flag=1)  # Ask again if the response is not 'y' or 'n'
    else:
        init_banner()
        restart_error()
        response = str(input(colorize_text("\n[!] DO YOU WANT TO RESTART? (y/n)\n\n>>> ", "yellow")))
        response = response.lower()
        if response == "n":
            print(colorize_text("\n[!] SCRIPT FINISHED\n", "cyan"))
        elif response == "y":
            main()  # Restart the main function
        else:
            restart(flag=1)  # Ask again if the response is not 'y' or 'n'

# Main function to run the script
def main():
    init_banner()
    ip = input(colorize_text("\n[-] Insert your IP address: ", "yellow"))
    ip_test = is_ip_address(ip)
    while ip_test == False:
        init_banner()
        error(0)  # Display an error message for an invalid IP address
        ip = input(colorize_text("\n[-] Insert your IP address: ", "yellow"))
        ip_test = is_ip_address(ip)  # Check the validity of the IP address

    port = input(colorize_text("\n[-] Insert a port: ", "yellow"))
    port_test = test_port(port)
    while port_test == False:
        init_banner()
        error(1)  # Display an error message for an invalid port
        print(f'\n{colorize_text("[-] Insert your IP address: ", "yellow")}{ip}')
        port = input(colorize_text("\n[-] Insert a port: ", "yellow"))
        port_test = test_port(port)  # Check the validity of the port

    shell = input(colorize_text("\n[-] Insert a shell type: ", "yellow"))

    init_banner()
    lang_answer = lang_list()  # Select a reverse shell language
    lang_ans_test = test_lang_ans(lang_answer)
    while lang_ans_test == False:
        init_banner()
        error(2)  # Display an error message for an invalid language answer
        lang_answer = lang_list()
        lang_ans_test = test_lang_ans(lang_answer)

    lang_answer = int(lang_answer)

    print("\n")
    # Generate the reverse shell command
    rev_shell = rev_shells(lang_answer, ip, port, shell)
    if rev_shell == 0:
        rev_shell = rev_shells_2(lang_answer, ip, port, shell)
    if rev_shell == 0:
        rev_shell = rev_shells_3(lang_answer, ip, port, shell)

    filename = export()  # Get the output file name
    write_to_file(rev_shell, filename)  # Write the reverse shell command to a file

    restart()  # Ask the user if they want to restart the script

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
