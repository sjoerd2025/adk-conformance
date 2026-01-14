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

"""Custom tools for tools_agent_002."""

import re
from typing import Any


def validate_email(email: str) -> bool:
  """Checks if the provided string is a valid email format."""
  email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return bool(re.match(email_regex, email))


def get_user_id(email: str) -> int:
  """Retrieves a user ID based on their email."""
  if not validate_email(email):
    raise ValueError("Invalid email format provided.")
  # Simple hash for testing purposes
  return abs(hash(email)) % 10000


def create_booking(
    user_id: int, is_confirmed: bool, details: str
) -> dict[str, Any]:
  """Creates a booking for a user.

  Args:
    user_id: The unique identifier for the user.
    is_confirmed: Whether the booking is confirmed.
    details: Any additional details for the booking.

  Returns:
    A dictionary containing the booking information and the types of the
    received arguments.
  """
  return {
      "user_id": user_id,
      "is_confirmed": is_confirmed,
      "details": details,
      "user_id_type": str(type(user_id)),
      "is_confirmed_type": str(type(is_confirmed)),
      "details_type": str(type(details)),
  }
