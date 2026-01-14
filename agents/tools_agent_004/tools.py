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

"""Custom tools for tools_agent_004 - Travel Planning with Advanced Parameters."""

from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class FlightPreferences(BaseModel):
  """Flight search preferences with advanced parameter types."""

  cabin_class: str = Field(
      default="economy",
      description=(
          "Preferred cabin class: economy, premium_economy, business, or first"
      ),
  )
  max_stops: int = Field(
      default=1,
      description="Maximum number of stops allowed (0 for direct flights only)",
  )
  preferred_airline: Optional[str] = Field(
      default=None,
      description=(
          "Preferred airline code (e.g., 'UA', 'AA'), or None for any airline"
      ),
  )
  flexible_dates: bool = Field(
      default=False,
      description="Whether to search nearby dates for better prices",
  )


class TripDetails(BaseModel):
  """Core trip information."""

  origin: str = Field(description="Departure city or airport code")
  destination: str = Field(description="Arrival city or airport code")
  departure_date: str = Field(description="Departure date in YYYY-MM-DD format")
  return_date: Optional[str] = Field(
      default=None,
      description="Return date in YYYY-MM-DD format, or None for one-way trip",
  )


def search_flights(
    trip: TripDetails, preferences: Optional[FlightPreferences] = None
) -> dict:
  """Search for flights based on trip details and preferences.

  This function demonstrates advanced parameter handling:
  - Pydantic models as parameters (trip, preferences)
  - Optional/nullable parameters (preferences, return_date, preferred_airline)
  - Default values (cabin_class, max_stops, flexible_dates)

  Args:
    trip: Core trip information including origin, destination, and dates.
    preferences: Optional flight preferences. If not provided, uses defaults.

  Returns:
    A dictionary containing search results and parameters received.
  """

  # Use default preferences if not provided
  if preferences is None:
    preferences = FlightPreferences()

  # Determine trip type
  trip_type = "round-trip" if trip.return_date else "one-way"

  # Build search summary
  result = {
      "trip_type": trip_type,
      "route": f"{trip.origin} to {trip.destination}",
      "departure_date": trip.departure_date,
      "return_date": trip.return_date,
      "cabin_class": preferences.cabin_class,
      "max_stops": preferences.max_stops,
      "preferred_airline": preferences.preferred_airline,
      "flexible_dates": preferences.flexible_dates,
      "search_status": "completed",
  }

  # Mock flight results
  airline = preferences.preferred_airline or "Various Airlines"
  stops_desc = (
      "direct"
      if preferences.max_stops == 0
      else f"up to {preferences.max_stops} stops"
  )

  result["available_flights"] = [
      (
          f"{airline} - {trip_type} {preferences.cabin_class} flight with"
          f" {stops_desc}"
      ),
      f"Departure: {trip.departure_date}",
  ]

  if trip.return_date:
    result["available_flights"].append(f"Return: {trip.return_date}")

  return result


def calculate_trip_cost(
    base_fare: float,
    num_passengers: int = 1,
    insurance: bool = False,
    baggage_count: Optional[int] = None,
) -> dict:
  """Calculate total trip cost with various optional charges.

  This function demonstrates:
  - Mix of required and optional parameters
  - Default values for common cases
  - Nullable parameter that affects calculation logic

  Args:
    base_fare: Base ticket price per passenger.
    num_passengers: Number of passengers (default: 1).
    insurance: Whether to add travel insurance (default: False).
    baggage_count: Number of checked bags per passenger, or None for carry-on
      only.

  Returns:
    A dictionary with cost breakdown.
  """
  subtotal = base_fare * num_passengers

  # Add insurance if requested (10% of base fare per passenger)
  insurance_cost = subtotal * 0.1 if insurance else 0.0

  # Add baggage fees if specified
  baggage_cost = 0.0
  if baggage_count is not None and baggage_count > 0:
    # First bag free, $35 per additional bag per passenger
    chargeable_bags = max(0, baggage_count - 1)
    baggage_cost = chargeable_bags * 35 * num_passengers

  total = subtotal + insurance_cost + baggage_cost

  return {
      "base_fare": base_fare,
      "num_passengers": num_passengers,
      "subtotal": subtotal,
      "insurance_included": insurance,
      "insurance_cost": insurance_cost,
      "baggage_count": baggage_count,
      "baggage_cost": baggage_cost,
      "total_cost": total,
  }
