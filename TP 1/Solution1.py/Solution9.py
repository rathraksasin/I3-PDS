def electricity_bill(kwh):
    # (a) Return None for negative input
    if kwh < 0:
        return None
        
    # Calculate consumption chunks per progressive tier
    tier1 = min(max(kwh, 0), 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)
    
    # Calculate energy cost based on tier rates
    energy_cost = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)
    
    # Add fixed service fee and apply 10% VAT
    total_bill = (energy_cost + 2000) * 1.10
    
    # Return rounded to a whole number
    return round(total_bill)


# (b) Print table for specific test values

print("EXPECTED OUTPUT")
test_cases = [0, 35, 50, 120, 200, 350]

for k in test_cases:
    bill_riel = electricity_bill(k)
    bill_usd = bill_riel / 4100
    # Formatting with thousands separators (:,) and fixed decimal positions (.2f)
    print(f"{k:3d} kWh -> {bill_riel:7,} riel  (= {bill_usd:6.2f} USD)")


# (c) Interactive User Prompt

print("\n--- Interactive Bill Calculator ---")
try:
    user_input = float(input("Enter your monthly consumption in kWh: "))
    result = electricity_bill(user_input)
    
    if result is None:
        print("Error: Consumption cannot be negative.")
    else:
        print(f"Your total bill is: {result:,} riel (= {result/4100:.2f} USD)")
except ValueError:
    print("Error: Please enter a valid number.")
