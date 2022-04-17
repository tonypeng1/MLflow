# ---
# jupyter:
#   jupytext:
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import plotly.express as px

df = px.data.iris()

fig = px.scatter(df,
                x = 'sepal_width',
                y = 'sepal_length',
                color = 'species')

fig.layout.title = 'The Iris Dataset<br>Title edited in VS Code'

fig.show()




