import prompts as prompts
import configs as cfg
def prompt_multi(question_type, prompt):
    if question_type == "多项选择题":
        return prompt + prompts.prompt_multi_choice 
    else:
        return prompt + prompts.prompt_single_choice 

def prompt_basic(question_type):
    prompt_tmp = prompts.prompt_praise + prompts.prompt_add[question_type] 
    return prompt_tmp + prompts.prompt

def prompt_add_analysis(db, query, prompt):
    analyses = db.similarity_search(k = cfg.similarity_search_k, query=query)
    prompt += prompts.prompt_add_analysis
    i = 1
    for analysis in analyses:
        prompt += "知识点" + str(i) + ": " + analysis.page_content + "\n"
        i += 1
    return prompt

def prompt_add_3_prev_q(db, q):
    return

def organize_query(q, db):
    question_type = q['question_type']
    db_analysis = db['db_analysis']
    db_prev_q = db['db_prev_q'] 
    q['options'] = '\n'.join([f"{k}:{v}" for k,v in q['option'].items()])
    prompt_tmp = prompt_basic(question_type)
    if db_analysis:
        # TODO: 精准搜索options里面的字，去掉选项字母
        prompt_tmp = prompt_add_analysis(db_analysis, q['question'] + q['options'], prompt_tmp)
    # if db_prev_q:
    #     prompt_tmp = prompt_add_3_prev_q(db_prev_q, q, prompt_tmp)
    prompt_tmp = prompt_multi(question_type, prompt_tmp)
    return prompt_tmp.format_map(q)