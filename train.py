# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import os
from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    log_param("param1", 5)
    
    log_metric("foo", 1)
    
    with open("output.txt", "w") as f:
              f.write("hellow world!")
              
    log_artifact("output.txt")

# %%
# !mlflow ui

# %%
