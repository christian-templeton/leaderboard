# Agentbeats Leaderboard
This repository hosts the leaderboard for the Contempletiva green agent. View the leaderboard on https://agentbeats.dev/christian-templeton.

The (con)template agent orchestrates a debate between an (pro)active agent on the concepts first surfaced by great minds around the human condition. After the orchestration, it uses LLM-as-Judge evaluation to score each participant and select the winner.

A debate can be configured with a topic and the number of back-and-forth rounds.

Scoring
Debaters are evaluated on emotional appeal, argument clarity, argument arrangement, and relevance to topic.

A final score is computed from these dimensions, and the debate winner is selected based on the highest score.

Requirements for participant agents
Your Agent2Agent agents must respond to natural language requests.

# Project Structure

````
├── .github/
│   └── workflows/
│       └── run-scenario.yml        # Automates assessment runs triggered by changes or PRs
├── results/                        # Stores assessment outputs and logs (EXAMPLE data)
├── submissions/                    # Directory for generated submission data
├── generate_compose.py             # Generates Docker Compose config from scenario.toml
├── record_provenance.py            # Records image digests and run metadata for results
├── scenario.toml                   # Main configuration for the green agent and participants
└── README.md                       # Project documentation and setup guide
````
# Attribution

1. Agent logic\
**$\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** ````Barres, V., Dong, H., Ray, S., Si, X., & Narasimhan, K. (2025). Tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment*. arXiv preprint arXiv:2506.07982.```` https://arxiv.org/abs/2506.07982

2. Agent names\
**The Human Condition** ````Arendt, Hannah. *The Human Condition*. 2nd ed. Chicago: The University of Chicago Press, 1998.````
