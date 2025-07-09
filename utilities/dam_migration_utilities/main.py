from rich.console import Console
from rich.table import Table
import os
import requests

# create a table
table = Table(title="URL List Status", style="bold blue")
table.add_column("URL", justify="left", style="cyan", no_wrap=True)
table.add_column("Valid URl", justify="right", style="magenta")
table.add_column("Http Status", justify="right", style="green")

# stats tables
stats_table = Table(title="Stats Table", style="bold blue")
stats_table.add_column("Total URLs", justify="right", style="cyan")
stats_table.add_column("Total CF URLs", justify="right", style="magenta")
stats_table.add_column("Total Neo URLs", justify="right", style="red")

# instantiate console.
console = Console()


def read_url_content():
    list_of_urls = []
    with open("urls.txt", "r", encoding="utf-8") as r:
        urls = r.readlines()
        for url in urls:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = ("https://" + url).strip()
                if url:
                    list_of_urls.append(url)
        return list_of_urls


def validate_urls(urls):
    valid_urls = []
    invalid_urls = []
    for url in urls:
        if "dl?shr=" in url:
            invalid_urls.append(url)
        else:
            valid_urls.append(url)
    # works on the stats table
    stats_table.add_row(
        str(len(urls)), str(len(valid_urls)), str(len(invalid_urls)))
    return valid_urls, invalid_urls


def request_url(url):
    # This function would normally make a request to the URL
    # and return the HTTP status code.
    if url:
        response = requests.get(url)
        return response.status_code


def request_urls(urls):
    for url in urls:
        status_code = request_url(url)
        if status_code == 200:
            table.add_row(url, "Yes", str(status_code))
        else:
            table.add_row(url, "No", str(status_code))


if __name__ == "__main__":

    urls = read_url_content()
    validate_urls(urls)
    request_urls(urls)
    # Print the stats table
    console.print(stats_table)
    console.print("Processing URLs...", style="bold green")
    # Print the main table
    console.print(table)
