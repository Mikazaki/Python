from colorama import init
from termcolor import colored
init()

guess = colored("""
 ██████╗ ██╗   ██╗███████╗███████╗███████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║
╚██████╔╝╚██████╔╝███████╗███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
""",'light_cyan')
the = colored("""
████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗  
   ██║   ██╔══██║██╔══╝  
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝
""",'red')
number = colored("""
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""",'magenta')
game = colored("""
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
""",'light_yellow')

logo = f"{guess}{the}{number}{game}"