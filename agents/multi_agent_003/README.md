# Multi Agent 003

This agent (`multi_agent_003`) demonstrates multi-agent delegation when
child-to-parent transfers are disallowed using only `LlmAgent`.

## Purpose

-   Tests the delegation workflow where a coordinator `LlmAgent` routes requests
    to specialized sub-agents
-   Validates that the next conversation round will be sent to the root agent
    when disallow_transfer_to_parent flag is set to "True" in a sub-agent.