# Question 2: Convert values to inches, feet and yards[cite: 1]

def convert_length(cm_val):
    inches = cm_val / 2.54
    feet = inches / 12
    yards = feet / 3
    return inches, feet, yards

# (i) 83 cm[cite: 1]
# (ii) 115.67 cm[cite: 1]
# (iii) 14.2 m -> 1420 cm[cite: 1]
values_in_cm = [83, 115.67, 14.2 * 100]

for val in values_in_cm:
    inc, ft, yd = convert_length(val)
    print(f"\n{val} cm:")
    print(f"Inches: {inc:.2f}")
    print(f"Feet: {ft:.2f}")
    print(f"Yards: {yd:.2f}")