import os
import argparse
from typing import Any

from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

DEFAULT_THREAD_ID = "default"
DEFAULT_PROVIDER = "openai"
DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "anthropic": "claude-3-5-sonnet-latest",
}


def build_agent(provider: str, model_name: str) -> Any:
    """Create a ReAct agent with chosen provider/model and Tavily search tool."""
    #TODO: Set up anthropic key as env variable and change statement to enable user use anthropic model
    if provider == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError(
                "Missing OPENAI_API_KEY. Set it in your environment or .env file."
            )
    else:
        raise ValueError("provider must be 'openai' or 'anthropic'")


    memory = MemorySaver()
    model = init_chat_model(f"{provider}:{model_name}")
    #place holder for future tool usage
    tools = []

    agent = create_agent(model, tools, checkpointer=memory)
    return agent


def repl(agent: Any, provider: str, model_name: str) -> None:
    """Interactive CLI loop with conversational memory."""
    print(
        f"LangChain ReAct Agent ({provider}:{model_name}). Type 'exit' to quit.\n"
    )
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        run_once(agent, user_input)

def run_once(agent: Any, user_input: str) -> None:
    """Run a single turn and stream the agent's output."""
    config = {"configurable": {"thread_id": DEFAULT_THREAD_ID}}
    input_message = {"role": "user", "content": user_input}

    for step in agent.stream({"messages": [input_message]}, config, stream_mode="values"):
        last = step["messages"][-1]
        try:
            last.pretty_print()
        except Exception:
            role = last.get("role", "assistant")
            content = last.get("content", "")
            print(f"[{role}] {content}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LangChain ReAct Agent CLI")
    parser.add_argument(
        "--provider", choices=["openai", "anthropic"], default=DEFAULT_PROVIDER,
        help="LLM provider to use"
    )
    #TODO: add model selection to argparser change model_name accordingly
    args = parser.parse_args()

    provider = args.provider
    model_name = DEFAULT_MODELS[provider]

    agent = build_agent(provider, model_name)
    repl(agent, provider, model_name)
