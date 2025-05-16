import json
import requests
import re
from typing import Optional

from models.ChatGPT import chatgpt_t, chatgpt_v

from models.QWQ_flow import QWQ_t, QWQ_v


def extract_answer(text):
    pattern = r'<answer>[^<]*?([ABCD])[^<]*?</answer>'
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
    pattern2 = r'[^<]*?([ABCD])[^<]*?'
    if 'Answer' in text[-20:]:
        text2 = text[-20:].replace('Answer', 'answer')
    else:
        text2 = text[-20:]

    matches = re.findall(pattern2, text2)
    if matches:
        return matches[0]    
    return "Invalid Answer"


def get_responds(client, prompt, images, mm_flag):
    if mm_flag:
        model_result_, usage  = client(prompt,images)
    else:
        model_result_, usage = client(prompt)

    model_result = model_result_['output']

    model_reasoning = model_result_['reasoning_content']

    if model_reasoning is None:        
        if '<think>' in model_result and '</think>' in model_result:
            pattern = r'<think>(.*?)</think>'
            model_reasoning = re.findall(pattern, model_result, re.DOTALL)[0]
            model_result = model_result.replace('<think>'+model_reasoning+'</think>', '')
        else:
            model_reasoning = None

    return model_result, model_reasoning, usage

def get_cline(model_type, model, json_flag=False, temperature=0.6, max_token=None):

    with open('./configs/model_key.json', 'r', encoding='utf-8') as f:
        model_keys = json.load(f)

    

    model_name = model_keys[model_type][model]["model_name"]
    model_url = model_keys[model_type][model]["base_url"]
    model_key = model_keys[model_type][model]["key"]



    temperature = temperature
    if model_type == 'llm':

        if model in ['qvq-max']:

            client  = QWQ_t([model_key], model_url, model_name_QWQ32=model_name, temperature_QWQ32=temperature, json_flag=False, max_token=max_token)
     
        elif model in ["gpt-4o", 'o4-mini', 'gemini-2.0-flash', 'gemini-2.0-flash-thinking-exp','claude-3-7-sonnet-thinking', 'gemini-2.5-pro-exp-03-25','claude-3-7-sonnet-20250219-thinking']:

            client = chatgpt_t([model_key], model_url, model_name_chatgpt=model_name, json_flag=False, max_tokens=max_token)
    else:
        if model in [ "gpt-4o", 'o4-mini', 'gemini-2.0-flash', 'gemini-2.0-flash-thinking-exp','claude-3-7-sonnet-thinking', 'gemini-2.5-pro-exp-03-25','claude-3-7-sonnet-20250219-thinking']:

            client = chatgpt_v([model_key], model_url, model_name_chatgpt=model_name, json_flag=False, max_tokens=max_token)

        elif model in ['qvq-max']:

            client  = QWQ_v([model_key], model_url, model_name_QWQ32=model_name, temperature_QWQ32=temperature, json_flag=False, max_token=max_token)

    return client

def run_api_openai(client,user_prompt, images, mm_flag):


    model_result, model_reasoning, usage = get_responds(client, user_prompt, images, mm_flag)


    return {"model_result":model_result, "model_reasoning":model_reasoning, 'usage':str(usage)}
