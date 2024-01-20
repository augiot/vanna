import argparse
import json
import time
import openai
# from sql_post_process import fix_select_column
import re
import os
import sqlite3
# from get_selfconsistent_output import get_sqls
from tqdm import tqdm

import sys
current_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(current_path))
sys.path.append(project_path)



openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "你是谁"}]
)
print(completion.choices[0].message.content)




    
