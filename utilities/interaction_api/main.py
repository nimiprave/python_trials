import streamlit as st
from datetime import datetime, timedelta, time
import interactionApiRequest


def post_payload(payload_body):
    response = interactionApiRequest.post_payload(payload_body)
    if response.status_code >= 200:
        st.success(f"Payload posted successfully! with status code: {response.status_code}",
                   icon="✅")
    else:
        st.error(f"Response Error:  {response.content}", icon="🚨")


# Show the UI fields .
st.markdown("# Create Api Interaction Payload and Post to the backend System")
payload = {}

# Section for choosing the payload
mainContainer = st.container(border=True)
mainContainer.header("Choose the Payload Type")
with mainContainer:
    # Capture Interaction Contact ID
    iContactOrigin = st.text_input(label="Interaction Contact Origin",
                                   value="SAP_C4C_BUPA",
                                   help="The origin of the interaction contact, e.g., SAP_HYBRIS_CONSUMER")
    payload["InteractionContactOrigin"] = iContactOrigin
    default_contactIds = ['20250616', '20250617']
    iContactIds = st.multiselect(
        label="Multiple Contact ID", options=default_contactIds)
    payload["InteractionContactIds"] = iContactIds

    # iContactId = st.text_input(label="Interaction Contact ID",
    #                            value="20250616",
    #                            help="The unique identifier for the interaction contact, e.g., 20190628")
    # payload["InteractionContactId"] = iContactId

    default_comm_medium = interactionApiRequest.load_comm_mediums().index("WEB")
    communicationMedium = st.selectbox(label="Communication Medium",
                                       options=interactionApiRequest.load_comm_mediums(),
                                       index=default_comm_medium,
                                       help="Select the communication medium used for the interaction")
    payload["CommunicationMedium"] = communicationMedium

    default_interaction_type = interactionApiRequest.load_interactions().index(
        "WEBSITE_REGISTRATION")
    interactionType = st.selectbox(label="Interaction Type",
                                   options=interactionApiRequest.load_interactions(),
                                   index=default_interaction_type,
                                   help="The Interaction Type to be created in the System")
    payload["InteractionType"] = interactionType

    marketingArea = st.text_input(label="Marketing Area",
                                  value="GLOBAL",
                                  help="The marketing area for the interaction, e.g., GLOBAL")
    payload["MarketingArea"] = marketingArea

    # Capture Interaction Time Stamp
   # Section for Experimenting.
    internalContainer = st.container(border=True)
    internalContainer.header("Select the Time Stamp")
    with internalContainer:
        # Capture date
        date = st.date_input("Select Date")

        # Capture time
        chosen_time = st.time_input("Select Time")

        # Combine date and time into a single datetime object
        datetime_obj = datetime.combine(date, chosen_time)

   # Convert datetime object to ISO format with UTC timezone
    interactionTimeStampUTC = datetime_obj.isoformat()
    payload["InteractionTimeStampUTC"] = interactionTimeStampUTC
    payload["input_date"] = date
    payload["input_time"] = chosen_time

    # number of interactions to be created
    interaction_count = st.number_input(label="No of Interactions to create",
                                        min_value=1,
                                        max_value=10,
                                        step=1,
                                        help="Interactions created with Timestamp seconds apart")
    payload["interaction_count"] = interaction_count

    # Payload Section:
    with st.expander("Payload Generated", expanded=False):
        payload_container = st.container(border=True)
        payload_container.header("Payload Generated")
        # payload_body = interactionApiRequest.create_payload(payload)
        payload_body = interactionApiRequest.multiple_contactid_payload(
            payload)
        payload_container.button(
            label="Post to backend", on_click=lambda: post_payload(payload_body))
        payload_container.write(payload_body)
