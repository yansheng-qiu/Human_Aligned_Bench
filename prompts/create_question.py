def creat_en_text_question(question, A, B, C, D):


    prompt = f'''
This section includes four types of questions: visual reasoning, definition judgment, analogical reasoning, and logical judgment. Candidates are required to select the most appropriate answer from four options.

question: {question}

options:
A: {A}

B: {B}

C: {C}

D: {D}

Please think step by step and output in the following format:

<answer>A or B or C or D</answer> 
'''
    return prompt

def creat_zh_text_question(question, A, B, C, D):



    prompt = f'''
本部分包括图形推理、定义判断、类比推理与逻辑判断四种类型的试题，在四个选项中选出一个最恰当的答案。

问题: {question}

选项：
A: {A}

B: {B}

C: {C}

D: {D}

请你一步一步的思考，并按以下格式输出：

<answer>A or B or C or D</answer> 
'''

    return prompt


def creat_zh_mm_question(question, question_img, A, A_img, B, B_img, C, C_img, D, D_img):
    images = []
    if question_img:
        images.extend(question_img)
    if A_img:
        images.extend(A_img)
    
    if B_img:
        images.extend(B_img)
    
    if C_img:
        images.extend(C_img)

    if D_img:
        images.extend(D_img)
    
    if '<image' in question or '<image' in A or '<image' in B or '<image' in C or '<image' in D:
        pass

    else:
        image_count = 1
        for image in question_img:
            question =  question + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in A_img:
            A = A + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in B_img:
            B = B + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in C_img:
            C = C + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in D_img:
            D = D + '\n' + f'<image {str(image_count)}>'
            image_count += 1



    prompt = f'''
本部分包括图形推理、定义判断、类比推理与逻辑判断四种类型的试题，在四个选项中选出一个最恰当的答案。
问题: {question}

选项：
A: {A}

B: {B}

C: {C}

D: {D}

请你一步一步的思考，并按以下格式输出：

<answer>A or B or C or D</answer> 
'''

    return prompt, images

def creat_en_mm_question(question, question_img, A, A_img, B, B_img, C, C_img, D, D_img):
    images = []
    if question_img:
        images.extend(question_img)
    if A_img:
        images.extend(A_img)
    
    if B_img:
        images.extend(B_img)
    
    if C_img:
        images.extend(C_img)

    if D_img:
        images.extend(D_img)
    

    if '<image' in question or '<image' in A or '<image' in B or '<image' in C or '<image' in D:
        pass
    else:
        image_count = 1
        for image in question_img:
            question =  question + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in A_img:
            A = A + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in B_img:
            B = B + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in C_img:
            C = C + '\n' + f'<image {str(image_count)}>'
            image_count += 1
        for image in D_img:
            D = D + '\n' + f'<image {str(image_count)}>'
            image_count += 1



    prompt = f'''
This section includes four types of questions: visual reasoning, definition judgment, analogical reasoning, and logical judgment. Candidates are required to select the most appropriate answer from four options.
question: {question}

options:
A: {A}

B: {B}

C: {C}

D: {D}

Please think step by step and output in the following format:

<answer>A or B or C or D</answer> 
'''


    return prompt, images