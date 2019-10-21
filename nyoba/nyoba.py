# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

path = 'outputs.json'
output_data = pd.read_json(path)
print(output_data.head)