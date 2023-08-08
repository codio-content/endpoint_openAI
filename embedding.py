import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN

import pandas as pd
import numpy as np
from openai.embeddings_utils import get_embedding, cosine_similarity

df = pd.read_csv("frankenstein.txt", sep="\n", header=None)
df["babbage_search"] = df.babbage_search.apply(eval).apply(np.array)

def search_text(df, text, n=3, pprint=True):
   embedding = get_embedding(
     text, 
     model='text-search-babbage-query-001')
   df['similarities'] = df.babbage_search.apply(lambda x: cosine_similarity(x, embedding))
   res = df.sort_values('similarities', ascending=False).head(n)
   return res

result = search_text(df, "scary monster")
print(result)

### CODIO SOLUTION END