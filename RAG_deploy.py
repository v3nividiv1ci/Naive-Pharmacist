from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_text_splitters.json import RecursiveJsonSplitter
from langchain.vectorstores import Chroma
import json

# TODO:写成一个类，然后load不同类型的资料（pdf/json）就继承这个类
# class RAG_loader():
#     def __init__():

# returns a list of dict
def load_json(file_path):
    with open(file_path) as f:
        list = json.load(f)
    rag_data = [i['analysis'] for i in list]
    return rag_data

def split_json(json_data):
    splitter = RecursiveJsonSplitter(max_chunk_size = 300)
    json_chunks = splitter.split_json(json_data = json_data)
    return json_chunks

def RAG_load_analysis(json_file):
    rag_data = load_json(json_file)
    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_texts(texts=rag_data, embedding=embedding)
    return vectordb

def RAG_load_prev_q():
    return