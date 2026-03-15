#!/bin/env python

import sys

for line in sys.stdin:
    print(line.strip())

sys.exit(0)


def get_input():
    return sys.stdin.readline().strip()


def get_output(*args):
    if len(sys.argv) > 1:
        return sys.stdout.write(sys.argv[1])
    return sys.stdout.write

def banner():
    get_output()
    get_output("Welcome to the Personal Notes service!\n")
    get_output("Please enter your username:\n")

def branding():
    # Dashing Feast in ASCII
    print("""
    __   __   __   __   __   __   __   __   __   __   __   __   __   __   __
    /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \ /  \
    \__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V\__V
    """)

    print("""
___________           .__                                         __  .__                    _______________________________
\__    ___/___   ____ |  |__    ____ ___.__._____    ____ _____ _/  |_|  |__   ____   ____   \_   ___ \__    ___/\_   _____/
  |    |_/ __ \_/ ___\|  |  \  / ___<   |  |\__  \  /    \\__  \\   __\  |  \ /  _ \ /    \  /    \  \/ |    |    |    __)  
  |    |\  ___/\  \___|   Y  \/ /_/  >___  | / __ \|   |  \/ __ \|  | |   Y  (  <_> )   |  \ \     \____|    |    |     \   
  |____| \___  >\___  >___|  /\___  // ____|(____  /___|  (____  /__| |___|  /\____/|___|  /  \______  /|____|    \___  /   
             \/     \/     \//_____/ \/          \/     \/     \/          \/            \/          \/               \/

          """)

if __name__ == "__main__":
    main()



