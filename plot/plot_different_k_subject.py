# 图1 : 横坐标: 按题型分类，每组里面又分k = 0, 1, 2, 4, 8；纵坐标: acc
# 图2 : 横坐标: 按题型分类，每组里面又分k = 0, 1, 2, 4, 8；纵坐标: acc
import matplotlib.pyplot as plt
import os
import sys
sys.path.append("..")
import configs as cfg
import prompts as prompts
import parse as p
import draw as d

if __name__ == "__main__":
    x_axis = cfg.model_list
    data_dir = '../data'
    fig_dir = '../figs'
    dir_different_k_gpt_4 = os.path.join(data_dir, 'different_k_gpt_4')
    total_acc, question_type_acc_dict, subject_acc_dict = p.parse(dir_different_k_gpt_4)
    print('total_acc', total_acc)
    print('question_type_acc_list', question_type_acc_dict)
    print('subject_acc_list', subject_acc_dict)
    # d.draw_different_k_question_type(fig_dir,question_type_acc_dict,total_acc)
    d.draw_different_k_subject(fig_dir, subject_acc_dict,total_acc)