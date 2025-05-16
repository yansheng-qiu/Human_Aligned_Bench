import time
from random import choice
from typing import List
from openai import OpenAI
import json

import os

import re

import base64

image_path = './dataset/images'

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

class  QWQ_v:
    def __init__(self, api_key_list_QWQ32, base_url_QWQ32, model_name_QWQ32="QWQ32-chat", temperature_QWQ32=0.6, json_flag=True, max_token=15000):
    

        self.api_key_list_QWQ32 = api_key_list_QWQ32
        self.base_url_QWQ32 = base_url_QWQ32



        self.model_name_QWQ32 = model_name_QWQ32
        self.temperature_QWQ32 = temperature_QWQ32

        self.json_flag = json_flag
        self.max_token = max_token

        
        

            
    def send_request(self, prompt, images):
        """
        """
        output = {}
        # while True:
        #     try:

        content = [{"type": "text","text": prompt}]
        for img in images:
            img_conten = encode_image(os.path.join(image_path,img))
            content.append({"type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{img_conten}"}})
            

        api_key_QWQ32 = choice(self.api_key_list_QWQ32)
        
        client_QWQ32 = OpenAI(api_key=api_key_QWQ32, base_url=self.base_url_QWQ32)

        messages = [
            {
                "role": "user",
                "content": content,
            },
        ]
        output = client_QWQ32.chat.completions.create(
            model=self.model_name_QWQ32,
            messages=messages,
            temperature=self.temperature_QWQ32,
            stream=True,
            max_tokens=self.max_token
        )

        reasoning_content = "" 
        answer_content = ""    
        is_answering = False 

        for chunk in output:
            if not chunk.choices:
                print("\nUsage:")
                print(chunk.usage)
            else:
                delta = chunk.choices[0].delta
                if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
                    reasoning_content += delta.reasoning_content
                else:
                    if delta.content != "" and is_answering is False:
                        is_answering = True
                    answer_content += delta.content



        reasoning_content = reasoning_content

        output = answer_content

        output = {'output':output,
                    'reasoning_content':reasoning_content}



        return output,reasoning_content

    def forward(self, prompt, images):

        model_output, usage= self.send_request(prompt, images)

        return model_output, usage
    
    def postprocess(self, output):
        model_output = None
        if isinstance(output, str):
            model_output = output
        else:
            content = output.choices[0].message.content
            content = re.sub(r'```json\n|\n```', '', content)
            content = re.sub(r'\njson\n|\n```', '', content)
            model_output = json.loads(content)
        return model_output

    def __call__(self, prompt, images):
        return self.forward(prompt, images)


class  QWQ_t:
    def __init__(self, api_key_list_QWQ32, base_url_QWQ32, model_name_QWQ32="QWQ32-chat", temperature_QWQ32=0.6, json_flag=True, max_token=15000):
    

        self.api_key_list_QWQ32 = api_key_list_QWQ32
        self.base_url_QWQ32 = base_url_QWQ32



        self.model_name_QWQ32 = model_name_QWQ32
        self.temperature_QWQ32 = temperature_QWQ32

        self.json_flag = json_flag
        self.max_token = max_token

        
        

            
    def send_request(self, prompt):

        output = {}




        api_key_QWQ32 = choice(self.api_key_list_QWQ32)
        
        client_QWQ32 = OpenAI(api_key=api_key_QWQ32, base_url=self.base_url_QWQ32)

        messages = [
            {
                "role": "user",
                "content": prompt,
            },
        ]
        output = client_QWQ32.chat.completions.create(
            model=self.model_name_QWQ32,
            messages=messages,
            temperature=self.temperature_QWQ32,
            stream=True,
            max_tokens=self.max_token
        )

        reasoning_content = "" 
        answer_content = ""    
        is_answering = False 

        for chunk in output:
            if not chunk.choices:
                print("\nUsage:")
                print(chunk.usage)
            else:
                delta = chunk.choices[0].delta
                if hasattr(delta, 'reasoning_content') and delta.reasoning_content != None:
                    reasoning_content += delta.reasoning_content
                else:
                    if delta.content != "" and is_answering is False:
                        is_answering = True
                    answer_content += delta.content



        reasoning_content = reasoning_content

        output = answer_content
        output = {'output':output,
                    'reasoning_content':reasoning_content}

        usage=None


        return output,usage

    def forward(self, prompt):

        model_output, usage = self.send_request(prompt)


        return model_output, usage
    
    def postprocess(self, output):
        model_output = None
        if isinstance(output, str):
            model_output = output
        else:
            content = output.choices[0].message.content
            content = re.sub(r'```json\n|\n```', '', content)
            content = re.sub(r'\njson\n|\n```', '', content)
            model_output = json.loads(content)
        return model_output

    def __call__(self, prompt:str):
        return self.forward(prompt)

