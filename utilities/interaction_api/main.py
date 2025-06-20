import streamlit as st
from datetime import datetime, timedelta, time
import interactionApiRequest

# Show the UI fields .
st.markdown("# Create Api Interaction Payload and Post to the backend System")

# {
#   "InteractionContactOrigin": "SAP_HYBRIS_CONSUMER",
#   "InteractionContactId": "20190628",
#   "CommunicationMedium": "WEB",
#   "InteractionType": "WEBSITE_REGISTRATION",
#   "InteractionTimeStampUTC": "2025-06-16T15:13:00",
#   "MarketingArea": "GLOBAL"
# }
# payload dictionary
payload = {}

# Section for choosing the payload
mainContainer = st.container(border=True)
mainContainer.header("Choose the Payload Type")
with mainContainer:
    # Capture Interaction Contact ID
    iContactOrigin = st.text_input(label="Interaction Contact Origin",
                                   value="SAP_HYBRIS_CONSUMER",
                                   help="The origin of the interaction contact, e.g., SAP_HYBRIS_CONSUMER")
    payload["InteractionContactOrigin"] = iContactOrigin

    iContactId = st.text_input(label="Interaction Contact ID",
                               value="20190628",
                               help="The unique identifier for the interaction contact, e.g., 20190628")
    payload["InteractionContactId"] = iContactId

    default_comm_medium = interactionApiRequest.load_comm_mediums().index("EMAIL")
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
    internalContainer.header("Capture Interaction Time Stamp")
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

    st.write("Interaction Time Stamp (UTC):", interactionTimeStampUTC)
    incremented_time = (datetime.combine(
        date, chosen_time) + timedelta(minutes=1)).time()
    incrementedtime_utc = datetime.combine(date, incremented_time)
    st.write("InteractionTime Incremented by 1 minute: ",
             incrementedtime_utc.isoformat())
    st.write(interactionApiRequest.create_payload(payload))
