from colorama import init
from termcolor import colored
init()

high = colored("""
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""",'light_cyan')

low = colored("""
██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
""",'magenta')
vs = colored("""
██╗   ██╗███████╗
██║   ██║██╔════╝
██║   ██║███████╗
╚██╗ ██╔╝╚════██║
 ╚████╔╝ ███████║
  ╚═══╝  ╚══════╝
                 """,color='red',attrs=['blink'])


logo = f"{high}{low}"