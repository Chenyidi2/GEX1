######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


# Airport info as a tuple (code, terminal, date)
airport_info = ("OUL", "1", "14-09-2026")

# Allowed gates as a set
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

# Restricted destinations as a set
restricted_destinations = {"Moscow", "Pyongyang"}

# Flights dictionary
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    cleaned = flight_number.strip().lower()
    for key in flights:
        if key.lower() == cleaned:
            return key
    return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    target = passenger_name.lower()
    for p in passengers:
        if p.lower() == target:
            return True
    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    name = passenger_name.strip().title()

    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    if name == "":
        return "EMPTY_NAME"

    if passenger_exists(flights[key]["passengers"], name):
        return "DUPLICATE"

    if len(flights[key]["passengers"]) >= flights[key]["capacity"]:
        return "FULL"

    if flights[key]["destination"] in restricted_destinations:
        return "RESTRICTED"

    flights[key]["passengers"].append(name)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    target = passenger_name.lower()
    for i, p in enumerate(flights[key]["passengers"]):
        if p.lower() == target:
            flights[key]["passengers"].pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    gate_upper = new_gate.upper()
    matched_gate = None
    for g in allowed_gates:
        if g.upper() == gate_upper:
            matched_gate = g
            break

    if matched_gate is None:
        return "INVALID_GATE"

    flights[key]["gate"] = matched_gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    num_passengers = len(flight["passengers"])
    capacity = flight["capacity"]
    percentage = num_passengers / capacity * 100

    if percentage == 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)
    if key is None:
        return None

    return sorted(flights[key]["passengers"])


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    count = 0
    for key in flights:
        count += len(flights[key]["passengers"])
    return count


# Logic to check if any flight is full
def any_full_flight(flights):
    for key in flights:
        if len(flights[key]["passengers"]) >= flights[key]["capacity"]:
            return True
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for key in flights:
        if len(flights[key]["passengers"]) == 0:
            return False
    return True
