from commons.dialogflowcx_answer import detect_intent_text
from commons.vertex_agent_search import (
    vertex_search_retail_products,
    vertex_search_fund_products
)
from commons.flex_message_builder import (
    build_products_search_result_carousel,
    generate_fund_flex_message,
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    ReplyMessageRequest,
    TextMessage,
    StickerMessage,
    FlexMessage,
    FlexContainer,
    ShowLoadingAnimationRequest,
    MentionSubstitutionObject,
    TextMessageV2,
    UserMentionTarget,
)
    
def handle_text_by_keyword(event, line_bot_api):
    text = event.message.text
        
    if text.startswith("#กองทุน"):
        search_query = text[len("#กองทุน") :].strip()
        response_dict = vertex_search_fund_products(search_query)
        print(response_dict)
        generate_fund_flex_message(
            line_bot_api=line_bot_api,
            event=event,
            response_dict=response_dict,
            search_query=search_query,
        )
    elif text.startswith("#fund"):
        search_query = text[len("#fund") :].strip()
        response_dict = vertex_search_fund_products(search_query)
        print(response_dict)
        generate_fund_flex_message(
            line_bot_api=line_bot_api,
            event=event,
            response_dict=response_dict,
            search_query=search_query,
        )
    elif text.startswith("#สินค้า"):
        search_query = text[len("#สินค้า") :].strip()
        response_dict = vertex_search_retail_products(search_query)
        print(response_dict)
        build_products_search_result_carousel(
            line_bot_api=line_bot_api,
            event=event,
            response_dict=response_dict,
            search_query=search_query,
        )
    else:
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text="please send image for product search, or to search fund type #fund and follow with fund you want to search")
                ],
            )
        )
        
        
