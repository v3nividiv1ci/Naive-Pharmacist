import matplotlib.pyplot as plt
import os
import sys
sys.path.append("..")
# from . import configs
import configs as cfg
import prompts as prompts

colors_different_models = ['lightsteelblue', 'slategrey']
color_different_k_question_type = ['y', 'lightsteelblue', 'cornflowerblue', 'royalblue', 'darkblue']
color_different_k_subject = ['orange', 'thistle', 'plum', 'violet', 'm']
question_type_2_Eng = {"最佳选择题": "q_best", "多项选择题": "q_multi", "综合分析选择题": "q_complex", "配伍选择题": "q_balance"}
subject_2_Eng = subject_type_list = {"药事管理与法规": "Pharmaceutical Management and Regulations", "药学综合知识与技能": "Comprehensive knowledge and skills of pharmacy", "药学专业知识（⼀）": "Pharmaceutical professional knowledge (I)", "药学专业知识（⼆）": "Pharmaceutical professional knowledge (II)"}

def draw_different_models(fig_dir, x_list):
    colors = colors_different_models
    x_len = len(x_list[0])
    x_param = list(range(x_len))
    name_list = list(x_list[0].keys())
    # print(name_list)
    total_width, n = 0.5, 2
    width = total_width / n 
    labels = ['no RAG', 'use RAG']
    for i, x in enumerate(x_list):
        assert x_len == len(x)
        key = str(x_list[i])
        if i == 0:
            plt.bar(x_param, list(x.values()),  width=width, label = labels[i],fc = colors[i], tick_label = name_list)
        else:
            plt.bar(x_param, list(x.values()),  width=width, label = labels[i],fc = colors[i])
        x_param = [p + width for p in x_param]
    title = "acc of different models with or without RAG"
    # 显示数据标签
    plt.title(title)
    # plt.ylim(0.5, 1)
    plt.xlabel("model")
    plt.ylabel("acc")
    plt.legend(loc=4)
    fig_name = os.path.join(fig_dir, title.replace(' ', '_') + '.jpg')
    plt.savefig(fig_name)
    return

def draw_different_k_question_type(fig_dir, x_dict, total_acc):
    # k = 0, 1, 2, 4, 8
    x_len = len(x_dict)
    t_list = prompts.question_type_list
    result_dict = {t : [0 for i in range(x_len)] for t in t_list}

    # ['k_0', 'k_1', 'k_2', 'k_4', 'k_8']
    k_list = ([k for k in x_dict.keys()])
    k_list.sort()
    x_param = list(range(x_len))
    x_param = [x * 2 for x in x_param]
    # total + 4种题型
    q_len = len(x_dict['k_0']) + 1

    # 把总体准确率按k = 0, 1, 2, 4, 8排序生成列表
    result_total = [0 for i in range(x_len)]
    for acc in total_acc:
        num = k_list.index(acc)
        result_total[num] = total_acc[acc]

    # 把各个题型按照k = 0, 1, 2, 4, 8的顺序生成列表，并存入字典
    for k in x_dict:
        num = k_list.index(k)
        for t in x_dict[k]:
            result_dict[t][num] = x_dict[k][t]

    colors = color_different_k_question_type
    total_width, n = 1.8, q_len
    width = total_width / n 

    tick_label = [k.replace('_', ' = ') for k in k_list]

    # 先画总体准确率
    marker_size = 4.
    plt.plot(tick_label, result_total, label = 'total', color = colors[0])
    plt.plot(tick_label, result_total, 'o', markersize=marker_size, color=colors[0])
    # 画各个题型准确率
    i = 1
    for t in result_dict:
        # key = str(x_list[i])
        plt.plot(tick_label, result_dict[t], label = question_type_2_Eng[t],color = colors[i])
        plt.plot(tick_label, result_dict[t], 'o', markersize=marker_size,color = colors[i])
        i += 1
    # plt.bar(x_param, result_total,  width=width, label = 'total',fc = colors[0])
    # x_param = [p + width for p in x_param]
    # # 画各个题型准确率
    # i = 1
    # for t in result_dict:
    #     # key = str(x_list[i])
    #     if i == 2:
    #         plt.bar(x_param, result_dict[t],  width=width, label = question_type_2_Eng[t],fc = colors[i], tick_label = tick_label)
    #     else:
    #         plt.bar(x_param, result_dict[t],  width=width, label = question_type_2_Eng[t],fc = colors[i])
    #     i += 1
    #     x_param = [p + width for p in x_param]
    title = "acc of different question type with different k for similarity search"
    # 显示数据标签
    plt.title(title)
    # plt.ylim(0.5, 1)
    plt.xlabel("k for similarity search")
    plt.ylabel("acc")
    plt.legend(loc=4)
    fig_name = os.path.join(fig_dir, title.replace(' ', '_') + '.jpg')
    plt.savefig(fig_name)
    return

def draw_different_k_subject(fig_dir, x_dict, total_acc):
    # k = 0, 1, 2, 4, 8
    x_len = len(x_dict)
    s_list = prompts.subject_type_list
    result_dict = {s.split('《')[1].split('》')[0] : [0 for i in range(x_len)] for s in s_list}

    # ['k_0', 'k_1', 'k_2', 'k_4', 'k_8']
    k_list = ([k for k in x_dict.keys()])
    k_list.sort()
    x_param = list(range(x_len))
    x_param = [x * 2 for x in x_param]
    # total + 4种题型
    q_len = len(x_dict['k_0']) + 1

    # 把总体准确率按k = 0, 1, 2, 4, 8排序生成列表
    result_total = [0 for i in range(x_len)]
    for acc in total_acc:
        num = k_list.index(acc)
        result_total[num] = total_acc[acc]

    # 把各个题型按照k = 0, 1, 2, 4, 8的顺序生成列表，并存入字典
    for k in x_dict:
        num = k_list.index(k)
        for t in x_dict[k]:
            print(t)
            result_dict[t][num] = x_dict[k][t]

    colors = color_different_k_subject
    total_width, n = 1.8, q_len
    width = total_width / n 

    tick_label = [k.replace('_', ' = ') for k in k_list]

    # 先画总体准确率
    marker_size = 4.
    plt.plot(tick_label, result_total, label = 'total', color = colors[0])
    plt.plot(tick_label, result_total, 'o', markersize=marker_size, color=colors[0])
    # 画各个题型准确率
    i = 1
    for t in result_dict:
        print("t: ", t)
        plt.plot(tick_label, result_dict[t], label = subject_2_Eng[t],color = colors[i])
        plt.plot(tick_label, result_dict[t], 'o', markersize=marker_size,color = colors[i])
        i += 1

    title = "acc of different subjects with different k for similarity search"
    # 显示数据标签
    plt.title(title)
    # plt.ylim(0.5, 1)
    plt.xlabel("k for similarity search")
    plt.ylabel("acc")
    plt.legend(loc=4)
    fig_name = os.path.join(fig_dir, title.replace(' ', '_') + '.jpg')
    plt.savefig(fig_name)
    return