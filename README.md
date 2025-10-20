# ArvindReactAgentStarterCode
## Read this article about ReAct Agent from IBM
https://www.ibm.com/think/topics/react-agent
## Full document of LangChain Agent
https://python.langchain.com/docs/tutorials/agents/

## This is a simple example of creating a no-tool-using agent. Command line gpt basically. Not exactly fitting the definition of ReACT agent, but serving as a great starting point.

## Initilize the virtual env

python3 -m venv .venv

## Activate ve
source .venv/bin/activate

## Install required dependencies
pip install -r requirements.txt

## Set environment variables on your local machine

export OPENAI_API_KEY=your_openai_key

export ANTHROPIC_API_KEY=your_anthropic_key

## Run agent (OpenAI by default)
python agent.py

## Homework

- Change build_agent function so that Anthropic can be used as a provider
- Update the CLI to accept a `--model` argument (provider-specific) so users can choose any supported model (e.g., OpenAI `gpt-4o`, `gpt-4o-mini`, or Anthropic `claude-3-5-sonnet-latest`).
- Add helpful `--help` examples and validate provider/model combinations.

## Learning Goal
- Get familar with python Argparser, if statement
- System var
- Generate API key for AI platform

