import os
import json
import datetime
from typing import Dict, List, Tuple
from util import  extract_answer, run_api_openai, get_cline
from prompts.create_question import creat_en_mm_question, creat_en_text_question, creat_zh_mm_question, creat_zh_text_question
from multiprocessing import Pool, cpu_count
from functools import partial
from tqdm import tqdm



def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def evaluate_single_question(question , model_name: str, temperature:float,  max_token=None) -> Dict:

    mm_flag = question['mm_flag']
    en_flag = question['en_flag']

    if mm_flag:
        model_type='vlm'
    else:
        model_type='llm'

    clinet = get_cline(model_type=model_type,json_flag=False,
        model=model_name,
        temperature=temperature,
        max_token=max_token)
    

    question_text = question['question']['question_text']
    A_text = question['options']['A']["options_text"]
    B_text = question['options']['B']["options_text"]
    C_text = question['options']['C']["options_text"]
    D_text = question['options']['D']["options_text"]


    question_img = question['question']['question_img']
    A_img = question['options']['A']["options_img"]
    B_img = question['options']['B']["options_img"]
    C_img = question['options']['C']["options_img"]
    D_img = question['options']['D']["options_img"]



    if en_flag:
        if mm_flag:
            prompt, images = creat_en_mm_question(question_text, question_img, A_text, A_img, B_text, B_img, C_text, C_img, D_text, D_img)
        else:
            prompt = creat_en_text_question(question_text, A_text, B_text, C_text, D_text)
            images = None
    else:
        if mm_flag:
            prompt, images = creat_zh_mm_question(question_text, question_img, A_text, A_img, B_text, B_img, C_text, C_img, D_text, D_img)
        else:
            prompt = creat_zh_text_question(question_text, A_text, B_text, C_text, D_text)
            images = None
    

    llm_response = run_api_openai(clinet, prompt, images, mm_flag)
    llm_answer = extract_answer(llm_response["model_result"])
    result = {
        "question_raw": question,
        "correct_answer": question['answer'],
        "llm_usage": str(llm_response["usage"]),
        "llm_answer": llm_answer,
        "llm_response": llm_response,
        "is_correct": llm_answer.lower() == question['answer'].lower()
    }

    
    return result


def evaluate_questions(question_dir: str,  model_name: str = "gpt-4o-mini", temperature: float= 0.0, max_token=None, output_dir=None) -> List[Dict]:


    with open(question_dir, 'r') as f:
        question_datas_ = json.load(f) 


    current_path = output_dir

    results = []

    if os.path.exists(current_path):

        question_datas = []

        with open(current_path, 'r') as f:
            current_results = json.load(f)
        results = current_results

        current_question_indexs = []

        for current_data in current_results:
            current_question_indexs.append(current_data["question_raw"]['index']) 
        
        for data in question_datas_:
            if data['index'] in current_question_indexs:
                pass
            else:
                question_datas.append(data)

    else:
        question_datas = question_datas_


    
    total_questions = len(question_datas)

    

    num_processes=5

    
    with Pool(num_processes) as pool:
        eval_func = partial(evaluate_single_question, model_name=model_name, temperature=temperature, max_token=max_token)
        for result in tqdm(
            pool.imap(eval_func, question_datas),
            total=total_questions,
            desc="Processing",
            ncols=100
        ):
            if result is not None:
                results.append(result)

    
    return results




def evaluate_one_model(question_dir: str, model_name: str, output_dir, temperature: float = 0.0, max_token: int = 15000):

    output_dir = os.path.join(output_dir, model_name + '.json')


    results = evaluate_questions(question_dir, model_name, temperature, max_token, output_dir)    

    
    save_json(results, output_dir)

def main():
    dataset_path = r'./dataset/'
    question_dir = os.path.join(dataset_path, 'text_data.json')
    temperature = 0.6
    max_token = 15000
    
    model_tobe_evaluated = ['gemini-2.5-pro-exp-03-25']
    output_dir = './output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)



    for model_name in model_tobe_evaluated:
        evaluate_one_model(question_dir, model_name, output_dir, temperature=temperature, max_token=max_token)

if __name__ == "__main__":
    main()
