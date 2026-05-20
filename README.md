# LangChain Search Agents Tutorial

This branch (`project/search-agent`) demonstrates how to build search agents using LangChain's `create_agent` interface. The tutorial progresses through three key concepts, showing how to evolve from a basic custom tool implementation to using structured outputs with built-in LangChain integrations.

## Learning Objectives

- Understand the LangChain `create_agent` interface
- Build custom tools using the `@tool` decorator
- Integrate third-party search APIs (Tavily)
- Use LangChain's built-in tool integrations
- Implement structured outputs with Pydantic models

## Commits Overview

| # | Commit | Title | What You'll Learn | Key Changes |
|---|--------|-------|-------------------|-------------|
| 1 | [7749d8d](https://github.com/rojan621/langchain-course/commit/7749d8df0720df5442ef7853c7a09ba7b0be88c6) | intro to search agents | Project setup, creating custom search tools with `@tool` decorator, direct Tavily API integration, building an agent with `create_agent`, invoking agents with messages | Initial project setup with dependencies, created custom `search` function using `@tool`, direct `TavilyClient` integration, created agent using `create_agent(model=llm, tools=tools)`, invoked agent with `HumanMessage` |
| 2 | [2867dbf](https://github.com/rojan621/langchain-course/commit/2867dbf258337f75ef3be42059fff4fee0bae241) | langchain tavily built in tool | Using LangChain's built-in tool integrations instead of custom tools, code simplification and best practices | Replaced custom `@tool` with `TavilySearch` from `langchain_tavily`, removed boilerplate code, cleaner implementation |
| 3 | [09dd01d](https://github.com/rojan621/langchain-course/commit/09dd01d814ecc8e467767805cb741b76d3146007) | added structured output | Implementing structured outputs with Pydantic models, type-safe agent responses using `response_format` parameter | Added `Source` and `AgentResponse` BaseModels, configured `response_format` in `create_agent`, enforced predictable output structure |

## Running the Code

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up environment variables:
   ```bash
   # Create a .env file with:
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

3. Run the agent:
   ```bash
   python main.py
   ```

## Example Query

The agent searches for AI engineer job postings in the Bay Area on LinkedIn:
```python
"search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
```

## Key Takeaways

- **Custom Tools**: You can create custom tools using the `@tool` decorator for specialized functionality
- **Built-in Integrations**: LangChain provides pre-built tools that reduce boilerplate and improve maintainability
- **Structured Outputs**: Using Pydantic models with `response_format` ensures type-safe, predictable agent responses
- **Agent Interface**: The `create_agent` function provides a simple, consistent interface for building agents with different capabilities
