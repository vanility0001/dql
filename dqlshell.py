import os
import ctypes
from dql.parse import parse
from dql.errors import ParseError
import sys

ctypes.windll.kernel32.SetConsoleTitleW("DQL Shell")

__version__ = 0.1

os.system("cls")
token = input("Enter token: ")
os.system("cls")
print(f"DQL ({__version__})")
print("Type 'HELP' for help.")
print("\n")

while True:
    try:
        cmd = input("dql > ")
        parsed = parse(cmd)

        if cmd.upper() == "HELP":
            print("You are using dql, the command-line interface for using the Discord API.")
        else:
            parsed = parse(cmd)
        pass

    except (KeyboardInterrupt, ParseError, Exception) as err:
        if isinstance(err, KeyboardInterrupt):
            ans = input("\nAre you sure you want to quit? (Y/n) ")

            if ans.lower() == "y":
                os.system("cls")
                sys.exit(0)
            else:
                pass

        elif isinstance(err, ParseError):
            print(f"Parser ERROR: {err}")

        else:
            print(f"Unknown ERROR: {err}")
