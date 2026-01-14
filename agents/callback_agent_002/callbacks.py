# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Callbacks for callback_agent_002."""

from typing import Optional

from google.adk.agents.callback_context import CallbackContext
from google.genai import types


def shortcut_agent_execution(
    callback_context: CallbackContext,
) -> Optional[types.Content]:
  """Shortcuts agent execution based on session state.

  This function checks if a conversation limit has been reached in the
  `callback_context.state`. If the limit is reached, it returns a
  `types.Content` object to skip the agent's run. Otherwise, it sets a flag
  in the state to indicate the limit has been reached for the next call and
  returns None, allowing the agent to run.

  Args:
    callback_context: The context containing session state.

  Returns:
    A `types.Content` object if the agent execution should be skipped,
    otherwise None.
  """
  # Check the condition in session state
  if "conversation_limit_reached" in callback_context.state:
    # Return Content to skip the agent's run
    return types.Content(
        parts=[
            types.Part(
                text="Sorry, you have reached the limit of the conversation."
            )
        ],
        role="model",
    )
  else:
    # Sets the state to "True" to skip the agent's run next time.
    callback_context.state["conversation_limit_reached"] = "True"
    return None
