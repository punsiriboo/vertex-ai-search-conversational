import os
from google.cloud import dialogflowcx_v3beta1 as dialogflow
from google.protobuf.json_format import MessageToDict

from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage,
)

def detect_intent_text(text, session_id, line_bot_api, reply_token, language_code="th"):
    
    project_id = os.environ["CONVERSATIONAL_AGENT_PROJECT_ID"]
    location_id = os.environ["CONVERSATIONAL_AGENT_LOCATION"]
    agent_id = os.environ["CONVERSATIONAL_AGENT_ID"]

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "privates/agent_sa.json"

    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    session_path = f"{agent}/sessions/{session_id}"

    client_options = None
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        client_options = {"api_endpoint": api_endpoint}

    session_client = dialogflow.SessionsClient(client_options=client_options)
    text_input = dialogflow.TextInput(text=text)
    query_input = dialogflow.QueryInput(text=text_input, language_code=language_code)
    request = dialogflow.DetectIntentRequest(
        session=session_path, query_input=query_input
    )
    response = session_client.detect_intent(request=request)
    response_dict = MessageToDict(response._pb)
    print(response_dict)
    
    
    def get_nested(data, keys, default=None):
        for key in keys:
            try:
                data = data[key]
            except (KeyError, IndexError, TypeError):
                return default
        return data


    line_resp_msgs = []
    keys = ['queryResult', 'generativeInfo', 'actionTracingInfo', 'actions', 2, 'agentUtterance', 'text']
    response_text = get_nested(response_dict, keys, default="BOT_FAILED: ไม่พบข้อมูล")
    line_resp_msgs.append(TextMessage(text=response_text))


    keys = ['queryResult', 'generativeInfo', 'actionTracingInfo', 'actions', 1, 'toolUse', 'outputActionParameters', '200', 'search_result']
    search_result = get_nested(response_dict, keys, default=[])
    print(search_result)

    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token=reply_token,
            messages=line_resp_msgs
        )
    )
