import os
import pyfiglet
from .io import IO

def get_main_banner(version):
    os.system('clear')
    
    figlet_text = pyfiglet.figlet_format("RSNIFFER", font="slant")
    
    banner = f"{IO.Fore.LIGHTRED_EX}{figlet_text}{IO.Style.RESET_ALL}"
    
    credit = f"Created by Ryhandd | Menu Mode Enabled | v{version}\n"
    
    return banner + credit