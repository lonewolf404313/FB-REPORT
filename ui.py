import os
import sys
import time
import random

GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'


def clear():
    os.system('clear')


def clear_screen():
    clear()


def banner():
    clear()

    art = f"""
{CYAN}
█████╗██████╗       ██████╗ 
    ██╔════╝██╔══██╗      ██╔══██╗
    █████╗  ██████╔╝█████╗██████╔╝
    ██╔══╝  ██╔══██╗╚════╝██╔══██╗
    ██║     ██████╔╝      ██║  ██║
    ╚═╝     ╚═════╝       ╚═╝  ╚═╝
{RESET}
{YELLOW}========================================
{WHITE}          FB AUTO REPORT 
{YELLOW}========================================{RESET}
"""
    print(art)


def show_banner():
    banner()


def menu():
    banner()

    print(f"{GREEN} [1] {WHITE}START REPORT{RESET}")
    print(f"{RED}   [2] {WHITE}STOP REPORT{RESET}")
    print(f"{CYAN}  [3] {WHITE}REPORT STATUS{RESET}")
    print(f"{YELLOW} [4] {WHITE}EXIT{RESET}")

    print(f"{YELLOW}========================================{RESET}")

    return input(f"\n{CYAN}Select option: {RESET}").strip()


def message(text, color=GREEN):
    print(f"\n{color}{text}{RESET}")


def pause():
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")


def run_visual_effect(stop_event):
    frames = ["|", "/", "-", "\\"]

    while not stop_event.is_set():
        for frame in frames:
            if stop_event.is_set():
                break

            print(
                f"\r{CYAN}[ BACKUP ENGINE ] {frame} Processing...{RESET}",
                end="",
                flush=True
            )

            time.sleep(0.15)

    print(f"\r{GREEN}[ BACKUP ENGINE ] Stopped.          {RESET}")
