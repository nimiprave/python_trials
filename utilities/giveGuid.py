# program to strip the hypens in the GUID
import re
from rich.console import Console
console = Console()


def strip_hyphens(guid):
    guid = re.sub(r'-', '', guid)
    return guid.upper()


def get_guid():

    guid = input(" Provide the GUID: ")
    if guid:
        console.print(strip_hyphens(guid), style="bold green")


if __name__ == "__main__":
    # Example usage
    get_guid()
