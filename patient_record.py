print("PATIENT RECORD")
name = input("Enter patient name:")
age = input("Enter age")
drug =  input("drug prescribed")
print()
print("PATIENT SUMMARY")
print("Name:", name)
print("Age:", age)
print("Drug:", drug)
# Convert age string to an integer number for comparison
if int(age) >= 65:
    print("ALERT; Geriatric patient. Verify renal function and adust dosage if needed.")
else: 
    print("Dosage: Standard adult dosing applies.")
# .lower() make sure it catches it even if typed as 'amoxicillin' or 'Amoxicillin'
if drug.lower() == "amoxicillin":
    print("SAFETY CHECKS: Confirm patient has no known pennicillin allergies before dispensing.")
    


