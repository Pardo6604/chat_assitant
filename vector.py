import os
import json
import pandas as pd
from langchain.schema import Document
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# Load and inspect
with open('train.json') as f:
    data = json.load(f)
df = pd.DataFrame(data)
print(df.head())

# Cast everything to string
df = df.astype(str)

# Embeddings + vector store setup
embeddings = OllamaEmbeddings(model='mxbai-embed-large')
db_dir = './chroma_langchain_db'

flag = False

# Only add once if the directory didn’t exist
if not os.path.exists(db_dir):

    flag = True

    documents, ids = [], []
    for i, row in df.iterrows():

        text = " ".join([
            row['building_id'],
            row['description'],
            row['bedrooms'],
            row['bathrooms'],
            row['display_address'],
            row['price'],
            row['features']
        ])

        documents.append(Document(page_content=text,
                                  metadata={
                                      'street_address': row['street_address'],
                                      'latitude': row['latitude'],
                                      'manager_id': row['manager_id'],
                                  }))
        ids.append(str(i))
    
    print('\n\nNumber of Documents',len(documents))
    print('Document 1:', documents[0].page_content, '\n\n')


vector_store = Chroma(
    collection_name='Buildings_Info',
    persist_directory=db_dir,
    embedding_function=embeddings
)

print('\n\nflag status:', flag)

if flag:
    vector_store.add_documents(documents=documents[:1000], ids=ids[:1000])


print("Document count:", vector_store._collection.count())


retriever = vector_store.as_retriever(search_kwargs={'k': 5})
