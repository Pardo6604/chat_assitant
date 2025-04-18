from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model='llama3.2')

template = '''
You are an expert for Edwins a company that help costumers 
find their new appartment your job is to answer questions 
about apartment rentals listing based on the listing content 
like text description, number of bedrooms, price, etc.

Here are some relevant information: {info}

Here is the question to answer: {question}
'''

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print('\n\n-------------------------------------')
    question = input('Hello, How can I help you?: ')
    print('\n\n')

    if question == 'quit':
        break
    
    info = retriever.invoke(question)
    
    print('=== Retrieved info ===')
    print(info)
    print('======================')
    
    result = chain.invoke({'info':info, 'question': question})
    print(result)

