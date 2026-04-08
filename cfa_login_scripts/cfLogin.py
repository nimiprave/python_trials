#!/usr/bin/env python3
import subprocess
from rich.console import Console
from rich.table import Table
import sys

# Tables for the output --START
target_table = Table(title="List of Available Targets")

# table columns
target_table.add_column("Region Number", style="green")
target_table.add_column("Regions", justify="right", style="cyan", no_wrap=True)
target_table.add_column("Api", style="magenta")

# instance of console for display
console = Console()
# Tables for the output --END


def user_input():
    region_no = input("Enter the region number: ")
    while int(region_no) < 1 and int(region_no) > len(region_dictionary()):
        print("Invalid region number. Please enter the correct region number or type exit to quit.")
        region_no = input("Enter the region number: ")
        if region_no.upper() == 'EXIT':
            print("Exiting the program")
            sys.exit(0)
    return region_no

# function to create the dictionary of Regions and their respective API


def region_dictionary():
    region_dict = {
        "1": {"dev": "https://api.cf.sap.hana.ondemand.com"},
        "2": {"qa": "https://api.cf.sap.hana.ondemand.com"},
        "3": {"stage": "https://api.cf.eu30.hana.ondemand.com"},
        "4": {"ha-stage": "https://api.cf.us10.hana.ondemand.com"},
        "5": {"ha-eu": "https://api.cf.eu10-004.hana.ondemand.com"},
        "6": {"ha-dev": "https://api.cf.eu12-001.hana.ondemand.com"},
        "7": {"us-prod": "https://api.cf.us30.hana.ondemand.com"},
        "8": {"eu-prod": "https://api.cf.eu11.hana.ondemand.com"},
        "9": {"ap-prod": "https://api.cf.ap10.hana.ondemand.com"},
        "10": {"jp-prod": "https://api.cf.jp10.hana.ondemand.com"},
        "11": {"cn-prod": "https://api.cf.cn40.platform.sapcloud.cn"},
        "12": {"ibc-cfa-dev-mta-provider": "https://api.cf.eu12-001.hana.ondemand.com"},
        "13": {"ibc-joule-playground-hx618aom": "https://api.cf.eu12.hana.ondemand.com"},
        "14": {"private-cloud-l2-simon-eu12": "https://api.cf.eu12.hana.ondemand.com"},
        "15": {"private-cloud-l2-sudhir-eu12": "https://api.cf.eu12.hana.ondemand.com"},
    }
    return region_dict


# function to create the table of Regions and their respective API
def create_region_table():
    region_dict = region_dictionary()
    for key, value in region_dict.items():
        region_name = list(value.keys())[0]
        api_url = value[region_name]
        target_table.add_row(key, region_name, api_url)


def cf_login(region_no):
    region_dict = region_dictionary()
    region_name = list(region_dict[region_no].keys())[0]
    api_url = region_dict[region_no][region_name]
    subprocess.run(["cf", "login", "--sso", "-a", api_url])


if __name__ == "__main__":

    # prepare to display the table for selection
    create_region_table()
    console.print(target_table)

    # get the user input
    region_no = user_input()

    # login to the selected region
    cf_login(region_no)
    console.print("Logged in successfully",
                  style="bold green", highlight=True),
    console.print("You can now use the cf commands",
                  style="bold green", highlight=True)
