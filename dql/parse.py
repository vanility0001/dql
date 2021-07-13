import ast
from typing import Tuple, Union

from .errors import ParseError

# Defining the list of keywords
KEYWORDS = [
    "SEND",
    "LEAVE",
    "CREATE",
    "AND",
    "WHERE",
    "OPTIONS",
    "HELP"
]

# Defining the types of Discord objects
TYPES = [
    "GUILD"
    "TEXT_CHANNEL"
]


# Converts a query into a method, URL and dictionary
def parse(query: str) -> Union[Tuple[str, str, dict], None]:
    # Defining the base URL
    base = "https://discord.com/api/"

    # Checking if the query is nothing
    if len(query) == 0 or query is None:
        raise ParseError("You must supply a query.")

    # Splitting the query into a list
    q = query.split()

    # Checking if the first word is a valid keyword
    if q[0].upper() not in KEYWORDS:
        raise ParseError("The first word is not a valid keyword.")

    # CREATE keyword handler
    if q[0].upper() == "CREATE":
 
        # Checking if the Discord TYPE exists in query
        if 2 > len(q):
            raise ParseError("Missing Discord TYPE.")

        if q[1].upper() == "GUILD":
            # Redefining the split so that we can load
            q = query.split(maxsplit=4)
            # Defining method & URL
            method = "POST"
            url = base + "guilds"

            # Checking if the WHERE keyword exists in query
            if 3 > len(q):
                raise ParseError("Missing WHERE keyword.")

            # Checking if the 3rd word in the query is a WHERE keyword
            if q[2].upper() != "WHERE":
                raise ParseError("No WHERE keyword in CREATE query.")

            # Checking if the OPTIONS keyword exists in query
            if 4 > len(q):
                raise ParseError("Missing OPTIONS keyword")

            # Checking if the 4th word in the query is a OPTIONS keyword
            if q[3].upper() != "OPTIONS":
                raise ParseError("No OPTIONS keyword in CREATE query.")

            # Converting options into dictionary
            try:
                data = ast.literal_eval(q[4])
            except (IndexError, Exception) as err:
                if isinstance(err, IndexError):
                    raise ParseError("Options for CREATE query were not provided.")
                else:
                    raise Exception(f"Unknown error. Exception: \n {err}")

        # HELP keyword handler
        elif q[0].upper() == "HELP":
            print("You are using dql, the command-line interface for using the Discord API.")
            return

        # Returning a tuple that fits the query
        return method, url, data
