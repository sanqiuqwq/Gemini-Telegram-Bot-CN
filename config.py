from google.genai import types
conf = {
    "error_info":           "Error\n一些错误 !\n请尝试联系机器人管理员 !",
    "before_generate_info": "🤖回答中🤖",
    "download_pic_notify":  "🤖加载图片🤖",
    "model_1":              "gemini-2.5-flash-preview-04-17",
    "model_2":              "gemini-2.5-pro-preview-05-06",
    "model_3":              "gemini-2.0-flash-preview-image-generation",#for draw
    "streaming_update_interval": 0.5,  # Streaming answer update interval (seconds)
}

safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_NONE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_NONE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="BLOCK_NONE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="BLOCK_NONE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_CIVIC_INTEGRITY",
        threshold="BLOCK_NONE",
    )
]

generation_config = types.GenerateContentConfig(
    response_modalities=['Text', 'Image'],
    safety_settings=safety_settings,
)
