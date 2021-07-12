import requests
from typing import Tuple
import dqlshell
from .errors import RequestError


# Send requesting to Discord's api
def send(args: Tuple[str, str, dict]):
    headers = {
        "Authorization": f"Bot {dqlshell.token}"
    }

    if args[0] == "POST":
        r = requests.post(args[1], headers=headers)
        print(r.json())

    else:
        raise RequestError(f"'{args[0]}' is not a valid method.")
