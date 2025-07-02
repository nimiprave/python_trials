import requests
import json
from dotenv import load_dotenv
import os
from rich.console import Console
import regex
from datetime import datetime, timedelta, time

# console instance
console = Console()

# load environment variables from .env file
load_dotenv()

# get the base URL and API key from environment variables
backend_system = os.getenv('BACKEND_SYSTEM')
odata_service = os.getenv('BACKEND_ODATA')
user_name = os.getenv('BACKEND_USER')
password = os.getenv('BACKEND_PWD')
entity = os.getenv("BACKEND_ENTITY")
host_url = f"{backend_system}{odata_service}"
post_url = f"{backend_system}{odata_service}/{entity}"

# print the host URL for debugging
console.print(f"Host URL: {host_url}")
# print the user name for debugging
console.print(f"User Name: {user_name}")
#  print the password for debugging (not recommended in production)
# Uncomment this line to see the password,
console.print(f"Password: {password}")
# print odata service for debugging
console.print(f"OData Service: {odata_service}")

# function to get the xsrf token from the response headers


def get_xsrf_token_session():
    # make a request to the service with a basic authentication
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-csrf-token': 'Fetch'
    }
    response = requests.head(
        host_url, auth=(user_name, password), headers=headers, verify=False)

    console.print(response.status_code)
    token = response.headers.get('X-CSRF-Token')
    # debugging output
    print(response.headers.get('set-cookie', ''))
    print(response.headers.get('set-cookie', '').split(';')[0].split('=')[1])

    # regex to extract the token from the set-cookie header
    sessionid = regex.search(
        r'SAP_SESSIONID[A-Z0-9_]+=([a-zA-Z0-9_%-]+)', response.headers.get('set-cookie', '')).group(0)
    # sessionid = response.headers.get('set-cookie', '')
    console.print(sessionid, style="red")
    console.print(token)

    return {
        "token":  token,
        "cookie": sessionid
    }


# function to get the json payload


def get_payload():
    payload = {
        "Interactions": [
            {
                "InteractionContactOrigin": "SAP_HYBRIS_CONSUMER",
                "InteractionContactId": "20190628",
                "CommunicationMedium": "WEB",
                "InteractionType": "WEBSITE_REGISTRATION",
                "InteractionTimeStampUTC": "2025-06-16T15:13:00",
                "MarketingArea": "GLOBAL"
            }
        ]
    }
    return payload

# load interactions from a file


def load_interactions():
    with open("interaction_type.txt", "r") as file:
        interactions = []
        for line in file:
            interaction = line.strip()
            if interaction:
                interactions.append(interaction)
    interactions.sort()
    return interactions


# load communication mediums from a file
def load_comm_mediums():
    with open("comm_medium.txt", "r") as file:
        mediums = []
        for line in file:
            medium = line.strip()
            if medium:
                mediums.append(medium)
    mediums.sort()
    return mediums


def read_payload():
    with open("payload.json", "r") as file:
        json_payload = file.read()
        console.print(json_payload)

# function to make a post call with the payload


def _post_payload():
    # csrf tokaen
    token = get_xsrf_token_session()
    # payload
    body = get_payload()
    console.print(f"Body: {body}")
    # headers for the post request
    headers = {
        'Content-Type': 'application/json',
        'x-csrf-token': token.get("token"),
        'Cookie': token.get('cookie')
    }

    # make the post request
    response = requests.post(
        post_url,
        auth=(user_name, password),
        headers=headers,
        data=json.dumps(body),
        verify=False
    )

    print(response.status_code)
    if response.status_code == 201:
        console.print("Payload posted successfully!", style="bold green")
    else:
        console.print(f"Response Error:  {response.content}")

# post payload to the backend system


def post_payload(body):
    # csrf tokaen
    token = get_xsrf_token_session()
    # payload
    console.print(f"Body: {body}")
    # headers for the post request
    headers = {
        'Content-Type': 'application/json',
        'x-csrf-token': token.get("token"),
        'Cookie': token.get('cookie')
    }

    # make the post request
    response = requests.post(
        post_url,
        auth=(user_name, password),
        headers=headers,
        data=json.dumps(body),
        verify=False
    )

    if response.status_code == 201:
        console.print("Payload posted successfully!", style="bold green")
    else:
        console.print(f"Response Error:  {response.content}")
    return response

# create payload from the UI dictionary object


def create_payload(ui_dictionary):
    payload = {
        "Interactions": []
    }
    if ui_dictionary["interaction_count"] > 1:
        # first element
        payload["Interactions"].append(_create_interaction(
            ui_dictionary, ui_dictionary["InteractionTimeStampUTC"]))
        loop_index = 2
        while (loop_index <= ui_dictionary["interaction_count"]):
            future_time_stamp = get_timestamp_utc(
                ui_dictionary["input_date"], ui_dictionary["input_time"], loop_index - 1)
            payload["Interactions"].append(_create_interaction(
                ui_dictionary, future_time_stamp))
            loop_index += 1
    else:
        payload["Interactions"].append(_create_interaction(
            ui_dictionary, ui_dictionary["InteractionTimeStampUTC"]))

    return payload

# multiple contact ids payload


def multiple_contactid_payload(ui_dictionary):
    payload = {
        "Interactions": []
    }

    multipleContactIds = ui_dictionary["InteractionContactIds"]
    for contactid in multipleContactIds:
        if ui_dictionary["interaction_count"] > 1:
            # first element
            payload["Interactions"].append(_create_interaction_contactid(
                ui_dictionary, contactid, ui_dictionary["InteractionTimeStampUTC"]))
            loop_index = 2
            while (loop_index <= ui_dictionary["interaction_count"]):
                future_time_stamp = get_timestamp_utc(
                    ui_dictionary["input_date"], ui_dictionary["input_time"], loop_index - 1)
                payload["Interactions"].append(_create_interaction_contactid(
                    ui_dictionary, contactid, future_time_stamp))
                loop_index += 1
        else:
            payload["Interactions"].append(_create_interaction_contactid(
                ui_dictionary, contactid, ui_dictionary["InteractionTimeStampUTC"]))

    return payload


# create interaction
def _create_interaction(ui_dictionary, time_stamp):
    interaction = {
        "InteractionContactOrigin": ui_dictionary["InteractionContactOrigin"],
        "InteractionContactId": ui_dictionary["InteractionContactId"],
        "CommunicationMedium": ui_dictionary["CommunicationMedium"],
        "InteractionType": ui_dictionary["InteractionType"],
        "InteractionTimeStampUTC": time_stamp,
        "MarketingArea": ui_dictionary["MarketingArea"]
    }
    return interaction


def _create_interaction_contactid(ui_dictionary, contactid, time_stamp):
    interaction = {
        "InteractionContactOrigin": ui_dictionary["InteractionContactOrigin"],
        "InteractionContactId": contactid,
        "CommunicationMedium": ui_dictionary["CommunicationMedium"],
        "InteractionType": ui_dictionary["InteractionType"],
        "InteractionTimeStampUTC": time_stamp,
        "MarketingArea": ui_dictionary["MarketingArea"]
    }
    return interaction


def get_timestamp_utc(date, chosen_time, minutes):
    incremented_time = (datetime.combine(
        date, chosen_time) + timedelta(minutes=minutes)).time()
    return datetime.combine(date, incremented_time).isoformat()


if __name__ == "__main__":
    # Example usage
    # _post_payload()
    read_payload()
    # get_xsrf_token()
