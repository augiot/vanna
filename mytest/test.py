import vanna
from vanna.remote import VannaDefault
import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(parent_dir)

# 将父级目录的父级目录添加到系统路径中
sys.path.append(project_dir)
print(project_dir)

# api_key = vanna.get_api_key('511451527@qq.com')
api_key = "9c4db3cb91e94a15bddf9dbede44abd9"

vanna_model_name = 'chinook' # This is the name of the RAG model. This is typically associated with a specific dataset.
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

# from vanna.flask import VannaFlaskApp
from src.vanna.flask import VannaFlaskApp
app = VannaFlaskApp(vn)
app.run(port=8018)