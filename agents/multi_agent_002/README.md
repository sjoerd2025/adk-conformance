# Multi Agent 002

This agent (`multi_agent_002`) demonstrates multi-agent delegation when
peer-to-peer transfers are disallowed using only `LlmAgent`.

## Purpose

-   Tests the delegation workflow where a coordinator `LlmAgent` routes requests
    to specialized sub-agents.
-   Tests the agent transfer behavior of sub-agents when the
    disallow_transfer_to_peers flag is set to "True".
-   Validates that the sub-agents will transfer control back to the parent
    agent before the conversation gets delegated to another sub-agent.