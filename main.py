from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters.json import RecursiveJsonSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

import os, json, re
import prompt_concat as p
import configs as cfg
import RAG_deploy as r
import gpt_init as gpt
import acc_test as act

os.environ["OPENAI_API_KEY"] = cfg.OPENAI_API_KEY
os.environ["OPENAI_BASE_URL"] = cfg.OPENAI_BASE_URL

def load_data():
    with open(cfg.exam) as f:
        data = json.load(f)
    # add question id progressively (0 ~ 99) to record the wrong question easilier
    id = 0
    for d in data:
        d['id'] = id
        id += 1
    # delete the 3 questions [20, 25, 65] with empty
    data = [d for d in data if d['id'] not in [20, 25, 65]]
    return data

def create_file():
    assert os.path.exists(cfg.data_path), "data path does not exist\n"
    file_name = os.path.join(cfg.data_path, cfg.data_file)
    print(file_name)
    assert not os.path.exists(file_name), "file already exists\n"
    os.mknod(file_name)
    return file_name

if __name__ == '__main__':
    files = {
            'file_analysis' : cfg.file_analysis, 
             'files_prev_q' : cfg.files_prev_q
            }
    dbs =   {
            'db_analysis' :r.RAG_load_analysis(files['file_analysis']),
            # 'db_analysis' : None,
            'db_prev_q' : None
            }
    # TODO: 持久化，希望通过不同方式load的数据都能放入一个数据库
    gpt = gpt.GPT4(model = cfg.model)
    act.test_accuracy(dbs = dbs, quests = load_data(), gpt = gpt, f_name = create_file())

