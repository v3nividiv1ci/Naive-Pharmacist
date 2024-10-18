import os
import sys
sys.path.append("..")
import prompts as prompts

def get_percentage(line):
    return round(float(line.split(': ')[1].split('%')[0]) / 100, 2)

def get_list(line):
    # TODO:写完get_list，返回错题list
    return

def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    total_acc = 0
    t_list = prompts.question_type_list
    t_wrong_dict = {t : [] for t in t_list}
    t_acc_dict = {t : 0 for t in t_list}
    # 按科目统计准确率
    s_list = prompts.subject_type_list
    s_wrong_dict = {s : [] for s in s_list}
    s_acc_dict = {s.split('《')[1].split('》')[0] : [] for s in s_list}
    for line in lines:
        if '总体准确率: ' in line:
            total_acc = get_percentage(line)
        if '- 准确率: ' in line:
            sub_title = line.split(' ')[0].split('\n')[0]
            if sub_title in t_list:
                t_acc_dict[sub_title] = get_percentage(line)
                t_wrong_dict[sub_title] = get_list(line)
            elif sub_title in s_list:
                sub_title = sub_title.split('《')[1].split('》')[0]
                s_acc_dict[sub_title] = get_percentage(line)
                s_wrong_dict[sub_title] = get_list(line)
    return total_acc, t_acc_dict, s_acc_dict, t_wrong_dict, s_wrong_dict

def parse(dir):
    acc = {}
    t_acc_dict = {}
    s_acc_dict = {}
    for filename in os.listdir(dir):
        if filename.startswith('acc_'):
            key = filename.split('acc_')[1].split('.txt')[0]
            acc[key], t_acc_dict[key], s_acc_dict[key], _, _ = process_file(os.path.join(dir, filename))
    return acc, t_acc_dict, s_acc_dict


