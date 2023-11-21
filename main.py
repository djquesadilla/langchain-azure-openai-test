import os

from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()


model = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    deployment_name="synthetic-users-dev-gpt-35-turbo",
)

message = HumanMessage(
    content="Translate this sentence from English to French. I love programming."
)

print(model([message]))