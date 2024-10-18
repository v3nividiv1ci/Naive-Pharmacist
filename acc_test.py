from tqdm import tqdm
import prompt_concat as p
import prompts as prompts
import configs as cfg
import re

# TODO: 写完process

def record_in_file(q, f):
    gpt_ans = str(q['gpt_ans']).replace('\n', '').replace(',', '').replace(' ', '')
    correct_ans = str(q['answer']).replace('\n', '').replace(',', '').replace(' ', '')
    f.write(f"question {q['id']}: gpt_answer is: {gpt_ans}, correct answer is: {correct_ans}\n")
    f.write(f"prompt: {q['prompt']}\n\n")
    return

def process_final_result(quests, f_name):
    total_num = len(quests)
    # 统计总体准确率
    total_num_correct = sum([1 for q in quests if q['correct'] == True])
    # 按问题类型统计准确率
    t_list = prompts.question_type_list
    t_total_dict = {t : [] for t in t_list}
    t_wrong_dict = {t : [] for t in t_list}
    # 按科目统计准确率
    s_list = prompts.subject_type_list
    s_total_dict = {s : [] for s in s_list}
    s_wrong_dict = {s : [] for s in s_list}
    # 遍历进行统计
    with open(f_name, "a") as f:
        for q in quests:
            is_correct = q['correct']
            q_type = q['question_type']
            s_type = q['source']
            id = q['id']
            if not is_correct:
                t_wrong_dict[q_type].append(id)
                s_wrong_dict[s_type].append(id)
                record_in_file(q, f)
            t_total_dict[q_type].append(id)
            s_total_dict[s_type].append(id)
    # 打印答题情况
    print("---------------------------------\n")
    print(f"总体准确率: {total_num_correct/total_num:.2%}, {total_num_correct} / {total_num}")
    print("---------------------------------\n")
    print("按问题类型统计准确率: \n")
    for t in t_wrong_dict:
        if len(t_total_dict[t]) != 0:
            print(f"{t} - 准确率: {(len(t_total_dict[t]) - len(t_wrong_dict[t]))/len(t_total_dict[t]):.2%}, {(len(t_total_dict[t]) - len(t_wrong_dict[t]))} / {len(t_total_dict[t])}, 错题: {t_wrong_dict[t]}")
        else: 
            print(f"{t} - 相关题目未出现")
    print("---------------------------------\n")
    print("按科目统计准确率: \n")    
    for s in s_wrong_dict:
        if len(s_total_dict[s]) != 0:
            print(f"{s} - 准确率: {(len(s_total_dict[s]) - len(s_wrong_dict[s]))/len(s_total_dict[s]):.2%}, {(len(s_total_dict[s]) - len(s_wrong_dict[s]))} / {len(s_total_dict[s])}, 错题: {s_wrong_dict[s]}")
        else:
            print(f"{s} - 相关题目未出现")
    return

def process_result(q):
    gpt_answer = get_ans(q['gpt_ans'])
    if gpt_answer == q['answer']:
        q['correct'] = True
    else: 
        q['correct'] = False
    return q
 
def get_ans(ans):
    match = re.findall(r'.*?([A-E]+(?:[、, ]+[A-E]+)*)', ans)
    if match:
        last_match = match[-1]
        return ''.join(re.split(r'[、, ，]+', last_match))
    return ''

def gpt_quest(q, gpt, db):
    prompt = p.organize_query(q, db)
    q['gpt_ans'] =  gpt.call(prompt, args = {})
    q['prompt'] = prompt
    q = process_result(q)
    return q
def test_accuracy(dbs, quests, gpt, f_name):
    for i, q in enumerate(tqdm(quests[:cfg.req_num])):
        quests[i] = gpt_quest(q, gpt, dbs)
    process_final_result(quests[:cfg.req_num], f_name)
    return
    