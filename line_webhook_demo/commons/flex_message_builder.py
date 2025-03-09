import json

from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage,
    FlexContainer,
    FlexMessage,
    FlexCarousel,
)



def build_products_flex_message(
    line_bot_api, event, response_dict, search_query, additional_explain=None
):
    flex_product_bubble = """ \
        {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "<PRODUCT_IMAGE_URL>",
                                        "size": "full",
                                        "aspectMode": "cover",
                                        "aspectRatio": "150:98",
                                        "gravity": "center"
                                    }
                                ],
                                "flex": 1
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "<PRODUCT_NUMBER>",
                                        "size": "xs",
                                        "color": "#ffffff",
                                        "align": "center",
                                        "gravity": "center"
                                    }
                                ],
                                "backgroundColor": "#f70405",
                                "paddingAll": "2px",
                                "paddingStart": "4px",
                                "paddingEnd": "4px",
                                "flex": 0,
                                "position": "absolute",
                                "offsetStart": "18px",
                                "offsetTop": "18px",
                                "cornerRadius": "100px",
                                "width": "30px",
                                "height": "25px"
                            }
                        ]
                    }
                ],
                "paddingAll": "0px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "contents": [],
                                        "size": "md",
                                        "wrap": true,
                                        "text": "<PRODUCT_NAME>",
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": "ราคา: <PRODUCT_PRICE> บาท",
                                        "color": "#ffffffcc",
                                        "size": "sm"
                                    }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "icon",
                                                "url": "https://developers-resource.landpress.line.me/fx/clip/clip14.png"
                                            },
                                            {
                                                "type": "text",
                                                "text": "Add to cart",
                                                "flex": 0,
                                                "color": "#ffffff",
                                                "offsetTop": "-2px",
                                                "offsetStart": "4px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "height": "40px",
                                "spacing": "sm",
                                "margin": "xxl",
                                "borderWidth": "1px",
                                "borderColor": "#ffffff",
                                "cornerRadius": "4px",
                                "action": {
                                    "type": "postback",
                                    "label": "add to cart",
                                    "data": "action=add_item&item_id=<PRODUCT_SKU>&item_name=<PRODUCT_NAME>&item_price=<PRODUCT_PRICE>&item_image_url=<PRODUCT_IMAGE_URL>"
                                }
                            }
                        ]
                    }
                ],
                "paddingAll": "20px",
                "backgroundColor": "#f70405"
            }
        }"""
    product_bubble_temple = json.loads(flex_product_bubble)

    summary_text = response_dict["summary"]["summaryText"]

    result_products_list = []
    for idx, result in enumerate(response_dict["results"]):
        product_name = result["document"]["structData"]["name"]
        product_price = result["document"]["structData"]["price"]
        product_image_url = result["document"]["structData"]["image_url"]
        product_sku = result["document"]["structData"]["sku"]

        product_bubble_json = (
            product_bubble_temple.replace("<PRODUCT_NAME>", product_name)
            .replace("<PRODUCT_PRICE>", str(product_price))
            .replace("<PRODUCT_IMAGE_URL>", product_image_url)
            .replace("<PRODUCT_SKU>", str(product_sku))
            .replace("<PRODUCT_NUMBER>", str(idx + 1))
        )

        result_products_list.append(FlexContainer.from_json(product_bubble_json))

    carousel_flex_message = FlexMessage(
        alt_text=f"ผลการค้นหาสินค้า: {search_query}",
        contents=FlexCarousel(
            type="carousel",
            contents=result_products_list,
        ),
    )

    messages_list = [
        TextMessage(text=summary_text),
        carousel_flex_message
    ]
    if additional_explain:
        messages_list.insert(0, TextMessage(text=additional_explain))

    line_bot_api.reply_message(
        ReplyMessageRequest(reply_token=event.reply_token, messages=messages_list)
    )

def build_fund_flex_message(
    line_bot_api, event, response_dict, search_query, additional_explain=None
)   :
    result_products_list = []
    for idx, result in enumerate(response_dict["results"]):
        fund_data = result["document"]["structData"]
        return1D_color = "#FF5555" if fund_data["return1D"] < 0 else "#00AA00"
        returnYTD_color = "#FF5555" if fund_data["returnYTD"] < 0 else "#00AA00"

        flex_message = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": fund_data["fundCode"],
                        "weight": "bold",
                        "size": "lg",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": fund_data["fundNameThai"],
                        "size": "sm",
                        "color": "#666666",
                        "wrap": True
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NAV",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{fund_data['NAV']} บาท",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "flex": 3
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "เปลี่ยนแปลง (1D)",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{fund_data['return1D']}%",
                                        "size": "sm",
                                        "color": return1D_color,
                                        "align": "end",
                                        "flex": 3
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ผลตอบแทน YTD",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{fund_data['returnYTD']}%",
                                        "size": "sm",
                                        "color": returnYTD_color,
                                        "align": "end",
                                        "flex": 3
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Risk Level",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 2
                                    },
                                    {
                                        "type": "text",
                                        "text": f"{fund_data['riskSpectrum']} (สูง)" if fund_data['riskSpectrum'] >= 5 else f"{fund_data['riskSpectrum']} (ปานกลาง)",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "flex": 3
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": f"ข้อมูล ณ วันที่ {str(fund_data['NAVDate'])[:4]}-{str(fund_data['NAVDate'])[4:6]}-{str(fund_data['NAVDate'])[6:]}",
                                "size": "xs",
                                "color": "#999999",
                                "flex": 1,
                                "align": "start"
                            }
                        ]
                    }
                ]
            }
        }

        json_object = json.dumps(flex_message)
        result_products_list.append(FlexContainer.from_json(json_object))

    carousel_flex_message = FlexMessage(
        alt_text=f"ผลการค้นหาสินค้า: {search_query}",
        contents=FlexCarousel(
            type="carousel",
            contents=result_products_list,
        ),
    )
    summary_text = response_dict["summary"]["summaryText"]
    messages_list = [
        TextMessage(text=summary_text),
        carousel_flex_message
    ]
    if additional_explain:
        messages_list.insert(0, TextMessage(text=additional_explain))

    line_bot_api.reply_message(
        ReplyMessageRequest(reply_token=event.reply_token, messages=messages_list)
    )
