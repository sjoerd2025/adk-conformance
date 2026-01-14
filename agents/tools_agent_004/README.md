# Tools Agent 004

This agent (`tools_agent_004`) demonstrates advanced function tool parameter
handling through a travel planning scenario.

## Purpose

-   Tests function tools with **Pydantic model parameters**
    (`FlightPreferences`, `TripDetails`)
-   Demonstrates **optional/nullable parameters** (`preferences`, `return_date`,
    `preferred_airline`, `baggage_count`)
-   Validates **default value handling** (`cabin_class="economy"`,
    `num_passengers=1`, `insurance=False`)
-   Verifies complex nested model serialization and deserialization

## Story: Travel Planning Assistant

The agent helps users plan trips by:

1.  **Flight Search** - Finding flights with customizable preferences:
    -   Core trip details (origin, destination, dates)
    -   Optional preferences (cabin class, max stops, preferred airline)
    -   Support for one-way or round-trip bookings
    -   Default values for common preferences

2.  **Cost Calculation** - Computing total trip costs with optional add-ons:
    -   Base fare calculation for multiple passengers
    -   Optional travel insurance (10% of base fare)
    -   Checked baggage fees (first bag free, $35 per additional bag)
    -   Clear cost breakdown

## Advanced Parameter Features Tested

### Pydantic Models as Parameters

```python
class FlightPreferences(BaseModel):
  cabin_class: str = "economy"
  max_stops: int = 1
  preferred_airline: Optional[str] = None
  flexible_dates: bool = False

class TripDetails(BaseModel):
  origin: str
  destination: str
  departure_date: str
  return_date: Optional[str] = None

def search_flights(trip: TripDetails, preferences: Optional[FlightPreferences] = None)
```

### Mix of Required and Optional Parameters

```python
def calculate_trip_cost(
    base_fare: float,              # Required
    num_passengers: int = 1,       # Optional with default
    insurance: bool = False,       # Optional with default
    baggage_count: Optional[int] = None  # Nullable
)
```

## Test Coverage

This agent tests that the ADK runtime correctly:

-   Serializes/deserializes nested Pydantic models
-   Handles optional parameters at function call time
-   Applies default values when arguments are omitted
-   Distinguishes between `None` (nullable) and default values
-   Passes complex objects through tool invocation pipeline
