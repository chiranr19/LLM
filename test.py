import os
from typing import List

from langchain.embeddings.vertexai import VertexAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.docstore.document import Document
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from client import llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import chainlit as cl
from transformers import pipeline
from pdf_retriver import user_retriever
from gcs_bucket import upload_blob


@cl.on_chat_start
async def start():
    welcome_message = "Please upload a file to begin!"
    files = None
    while files is None:
        # Ask user to upload a file
        files = await cl.AskFileMessage(
            content=welcome_message,
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    # Get the first file
    file = files[0]

    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()
    print(file.name)
    print(file.path)

    # Upload the file into the GCS bucket using file content
    upload_blob('chainlit_rag-bucket', file.path, file.name)

    print(file.name)
    
    # Modify user_retriever to pass the location of the GCS file instead of file name
    retriever = user_retriever(f'{file.name}')

    template = """
    You are an information retrieval AI. Format the retrieved information as a table or text.
    
    Use only the context for your answers, do not make up information.
    
    query: {query}
    
    {context}
    """
    # Converts the prompt into a prompt template
    prompt = ChatPromptTemplate.from_template(template)

    # Using OpenAI model, by default GPT-3.5 Turbo
    model = llm

    chain = (
        {"context": retriever, "query": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    msg.content = f"`{file.name}` processed!"
    await msg.update()
    cl.user_session.set("chain", chain)

     # Let the user know that the system is ready
    msg.content = f"Processing `{file.name}` done. You can now ask questions!"
    await msg.update()

    cl.user_session.set("chain", chain)

    
@cl.on_message
async def main(message: cl.Message):
    # Retrieve the RAG chain from the user session
    chain = cl.user_session.get("chain")  # This gets the chain object set in the first code block

    # Execute the chain to get the answer synchronously (no dictionary, just the query string)
    res =  chain.invoke(message.content)  # Pass message.content as a string, not a dict

    # Extract the answer from the response
    answer = res # Extract the answer (could be 'answer' depending on the implementation)

    # Send the message with the answer only
    await cl.Message(content=answer).send()



# @cl.on_message
# async def main(message: cl.Message):
#     chain = cl.user_session.get("chain")  # type: ConversationalRetrievalChain
#     cb = cl.AsyncLangchainCallbackHandler()

#     res = await chain.acall(message.content, callbacks=[cb])
#     answer = res["answer"]
#     source_documents = res["source_documents"]  # type: List[Document]

#     text_elements = []  # type: List[cl.Text]

#     if source_documents:
#         for source_idx, source_doc in enumerate(source_documents):
#             source_name = f"source_{source_idx}"
#             # Create the text element referenced in the message
#             text_elements.append(
#                 cl.Text(content=source_doc.page_content, name=source_name, display="side")
#             )
#         source_names = [text_el.name for text_el in text_elements]

#         if source_names:
#             answer += f"\nSources: {', '.join(source_names)}"
#         else:
#             answer += "\nNo sources found"

#     await cl.Message(content=answer, elements=text_elements).send()
