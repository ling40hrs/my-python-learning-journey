'''Simple interest calculator with extra challenge.'''


import math

print("--- Simple Interest Calculator ---")
principal_amount_input = input("Enter the initial principal amount: > ")
interest_input = input("Enter the annual interest rate (e.g., 5 for 5%): > ")
number_years_inp = input("Enter the number of years: > ")

principal_amount_flt = float(principal_amount_input)
interest_flt =  float(interest_input) / 100
number_years_flt = float(number_years_inp)

print("--- Calculating... ---?")

p = principal_amount_flt
r = interest_flt
t = number_years_flt

for count in range(math.ceil(t)):
    si = p * r * 1

    total = si + p

    print(f"Year {(int(count)+1)}: Interest Earned: ${si} | End of Year Balance: ${total}")
    p = total

print(f"""--- Final Summary ---
      After {t} years, your initial deposit of ${principal_amount_flt} grew to ${total}.
      """)

for i in range(10,0,-1):
    print(i)
