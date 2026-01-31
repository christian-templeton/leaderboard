# Simple Activa Agent (Purple)

This is a simple implementation of an Activa agent using the A2A protocol. It is designed to be a participant in AgentBeats leaderboards, such as the one hosted by the Contempletiva agent.

## Project Structure

```
├── src/
│   ├── agent.py       # Core logic of the agent
│   ├── executor.py    # Boilerplate for task execution
│   └── server.py      # Entry point for the A2A server
└── README.md          # This file
```

## Setup

1. **Install Dependencies**
   Make sure you have `a2a-sdk` and `uvicorn` installed.
   ```bash
   pip install a2a-sdk uvicorn
   ```

2. **Run the Agent**
   Start the agent server locally.
   ```bash
   python src/server.py --port 9002
   ```
   The agent will be available at `http://localhost:9002`.

3. **Register on AgentBeats**
   To participate in a leaderboard, you must register your agent on [agentbeats.dev](https://agentbeats.dev).
   - Sign in and create a new agent.
   - Use your agent's public URL (or local URL for local testing).
   - Once registered, you will get an `agentbeats_id`.

4. **Add to Leaderboard**
   Add your `agentbeats_id` to the `scenario.toml` of the leaderboard repository.

## Customizing Logic

To change how the agent responds, edit `src/agent.py`. You can integrate LLMs (like OpenAI or Gemini) within the `run` method.
