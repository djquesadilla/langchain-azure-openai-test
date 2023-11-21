# Testing Langchain with Azure Open AI

It's very confusing, indeed.

## Starting up

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## .env file

```
# The base URL for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
AZURE_OPENAI_ENDPOINT=https://synthetic-users-dev.openai.azure.com/
# The API key for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
OPENAI_API_KEY=fac4ec9b97ed4f38baac612beaa56b07
```