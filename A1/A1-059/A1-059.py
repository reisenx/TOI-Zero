# --------------------------------------------------
# File Name : A1-059.py
# Problem   : Thunder Delivery
# Author    : Worralop Srichainont
# Date      : 2026-01-02
# --------------------------------------------------

# Define routes with (service fees, weight cost per kg)
ROUTES = {
    "BKK": {"CNX": (10.0, 30.0), "PKT": (25.0, 50.0)},
    "CNX": {"UBP": (15.0, 40.0)},
    "UBP": {"BKK": (20.0, 40.0), "PKT": (40.0, 70.0)},
    "PKT": {"CNX": (30.0, 60.0)},
}

# Read delivery details
start_location, stop_location = input().strip().split()
package_weight = float(input().strip())

# Find and calculate total delivery cost
if start_location in ROUTES and stop_location in ROUTES[start_location]:
    # Get service fees and weight cost
    service_fees, weight_cost = ROUTES[start_location][stop_location]

    # Calculate total cost
    total_cost = (weight_cost * package_weight) + service_fees
    print(f"{total_cost:.2f}")

# Route not found
else:
    print("Error")
