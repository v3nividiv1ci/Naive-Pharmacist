# 横坐标: 不同的模型（每组里面有两个：no rag和k = 2）；纵坐标: acc
# import matplotlib as plt
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
    dir_no_RAG = os.path.join(data_dir, 'different_model_no_RAG')
    dir_k_2 = os.path.join(data_dir, 'different_model_k_2')
    acc_no_RAG, _, _ = p.parse(dir_no_RAG)
    acc_k_2, _, _ = p.parse(dir_k_2)
    d.draw_different_models(fig_dir, [acc_no_RAG, acc_k_2])