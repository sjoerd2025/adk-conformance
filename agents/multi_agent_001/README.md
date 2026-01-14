# Multi Agent 001

This agent (`multi_agent_001`) demonstrates multi-agent delegation using only
`LlmAgent` types.

## Purpose

-   Tests the delegation workflow where a coordinator `LlmAgent` routes requests
    to specialized sub-agents
-   Demonstrates subject-based routing logic (math, science, history)
-   Verifies that the coordinator can delegate to one or multiple sub-agents
    based on the question
-   Validates proper aggregation of responses from multiple sub-agents
