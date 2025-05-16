


def creat_self_knowledge_figural_reasoning(en_flag):
    if en_flag:
        prompt = '''
Please help me summarize the core knowledge points and problem-solving methods of visual reasoning.
'''
    else:
        prompt = f'''
请你帮我总结图形推理的核心知识点以及做题方法
'''
        
    return prompt




def creat_self_knowledge_definition_judgment(en_flag):
    if en_flag:
        prompt = '''
Please help me summarize the core knowledge points and problem-solving methods of definition judgment.
'''
    else:
        prompt = f'''
请你帮我总结定义判断的核心知识点以及做题方法
'''
        
    return prompt



def creat_self_knowledge_analogical_reasoning(en_flag):
    if en_flag:
        prompt = '''
Please help me summarize the core knowledge points and problem-solving methods of analogical reasoning.
'''
    else:
        prompt = f'''
请你帮我总结类比推理的核心知识点以及做题方法
'''
        
    return prompt


def creat_self_knowledge_logical_judgment(en_flag):
    if en_flag:
        prompt = '''
Please help me summarize the core knowledge points and problem-solving methods of logical judgment.

'''
    else:
        prompt = f'''
请你帮我总结逻辑判断的核心知识点以及做题方法

'''
        
    return prompt


