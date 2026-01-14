# Loop Agent 001

This agent (`loop_agent_001`) demonstrates the use of a `LoopAgent` for
iterative email campaign optimization.

## Purpose

-   Tests the iterative workflow of a `LoopAgent` which repeatedly executes
    sub-agents until a completion condition is met
-   Demonstrates progressive refinement through multiple loop iterations (up to
    4 aspects: Clarity, Professionalism, Engagement, Brevity)
-   Verifies that state and improvements accumulate correctly across iterations
-   Tests the `exit_loop` tool for controlled loop termination
-   Validates max_iterations boundary condition
