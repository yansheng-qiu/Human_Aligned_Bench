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

class  chatgpt_v:
    def __init__(self, api_key_list_chatgpt, base_url_chatgpt, model_name_chatgpt="chatgpt-chat", temperature_chatgpt=0.6, json_flag=False, max_tokens=5000):
    

        self.api_key_list_chatgpt = api_key_list_chatgpt
        self.base_url_chatgpt = base_url_chatgpt



        self.model_name_chatgpt = model_name_chatgpt
        self.temperature_chatgpt = temperature_chatgpt

        self.json_flag = json_flag
        self.max_tokens = max_tokens

        
        

            
    def send_request(self, prompt, images):
        """
        """
        content = [{"type": "text","text": prompt}]
        for img in images:
            img_conten = encode_image(os.path.join(image_path,img))
            content.append({"type": "image_url",
                            "image_url": {"url": f"data:image/png;base64,{img_conten}"}})
            

        # output = ''
        # usage = None
        while True:
            try:
                api_key_chatgpt = choice(self.api_key_list_chatgpt)
                
                client_chatgpt = OpenAI(api_key=api_key_chatgpt, base_url=self.base_url_chatgpt)

                messages=[
                    {
                    "role": "user",
                    "content":content
                    }
                ]



                if self.model_name_chatgpt in ['o4-mini']:
                    output = client_chatgpt.chat.completions.create(
                        model=self.model_name_chatgpt,
                        messages=messages,
                        temperature=self.temperature_chatgpt,
                        stream=False,
                        max_completion_tokens=self.max_tokens 
                    )
                else:            
                    output = client_chatgpt.chat.completions.create(
                        model=self.model_name_chatgpt,
                        messages=messages,
                        temperature=self.temperature_chatgpt,
                        stream=False,
                        max_tokens=self.max_tokens 
                    )

                usage = output.usage

                if self.json_flag:

                    if hasattr(output.choices[0].message, 'reasoning_content'):
                        reasoning_content = output.choices[0].message.reasoning_content
                    else:
                        reasoning_content = None
                    output = self.postprocess(output)

                    
                else:
                    if hasattr(output.choices[0].message, 'reasoning_content'):
                        reasoning_content = output.choices[0].message.reasoning_content
                    else:
                        reasoning_content = None
                    output = output.choices[0].message.content
                
                output = {'output':output,
                         'reasoning_content':reasoning_content}


                break
            except Exception as e:
                print('Exception:', e)
                time.sleep(4)

        return output, usage

    def forward(self, prompt, images):

        model_output, usage= self.send_request(prompt, images)

        
        # time.sleep(2)
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





class  chatgpt_t:
    def __init__(self, api_key_list_chatgpt, base_url_chatgpt, model_name_chatgpt="chatgpt-chat", temperature_chatgpt=0.6, json_flag=False, max_tokens=2000):
    

        self.api_key_list_chatgpt = api_key_list_chatgpt
        self.base_url_chatgpt = base_url_chatgpt



        self.model_name_chatgpt = model_name_chatgpt
        self.temperature_chatgpt = temperature_chatgpt

        self.json_flag = json_flag

        self.max_tokens = max_tokens

        
        

            
    def send_request(self, prompt):
        """
        """
        output = {}
        while True:
            try:
 
                api_key_chatgpt = choice(self.api_key_list_chatgpt)
                
                client_chatgpt = OpenAI(api_key=api_key_chatgpt, base_url=self.base_url_chatgpt)

                # pass
                messages = [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]

                if self.model_name_chatgpt in ['o4-mini']:
                    output = client_chatgpt.chat.completions.create(
                        model=self.model_name_chatgpt,
                        messages=messages,
                        temperature=self.temperature_chatgpt,
                        stream=False,
                        max_completion_tokens=self.max_tokens 
                    )
                else:            
                    output = client_chatgpt.chat.completions.create(
                        model=self.model_name_chatgpt,
                        messages=messages,
                        temperature=self.temperature_chatgpt,
                        stream=False,
                        max_tokens=self.max_tokens 
                    )
                usage = output.usage


                if self.json_flag:

                    if hasattr(output.choices[0].message, 'reasoning_content'):
                        reasoning_content = output.choices[0].message.reasoning_content
                    else:
                        reasoning_content = None
                    output = self.postprocess(output)

                    
                else:
                    if hasattr(output.choices[0].message, 'reasoning_content'):
                        reasoning_content = output.choices[0].message.reasoning_content
                    else:
                        reasoning_content = None
                    output = output.choices[0].message.content
                
                output = {'output':output,
                         'reasoning_content':reasoning_content}



                break
            except Exception as e:
                print('Exception:', e)
                time.sleep(4)

        return output, usage

    def forward(self, prompt):

        model_output, usage = self.send_request(prompt)

        
        # time.sleep(2)
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
