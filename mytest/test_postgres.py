import os
import sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(parent_dir)

# 将父级目录的父级目录添加到系统路径中
sys.path.append(project_dir)
print(project_dir)

from src.vanna.vannadb.vannadb_vector import VannaDB_VectorStore
from src.vanna.base import VannaBase

class MyCustomLLM(VannaBase):
    def __init__(self, config=None):
        pass

    def generate_plotly_code(self, question: str = None, sql: str = None, df_metadata: str = None, **kwargs) -> str:
        # Implement here
        pass

    def generate_question(self, sql: str, **kwargs) -> str:
        # Implement here
        pass
    def get_followup_questions_prompt(self, question: str, question_sql_list: list, ddl_list: list, doc_list: list, **kwargs):
        # Implement here
        pass
    def get_sql_prompt(self, question: str, question_sql_list: list, ddl_list: list, doc_list: list, **kwargs):
        # Implement here
        pass
    def submit_prompt(self, prompt, **kwargs) -> str:
        # Implement here
        pass

class MyVanna(VannaDB_VectorStore, MyCustomLLM):
    def __init__(self, config=None):
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key=MY_VANNA_API_KEY, config=config)
        MyCustomLLM.__init__(self, config=config)

vn = MyVanna()