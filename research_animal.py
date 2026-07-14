print("==============================")
print("     RESEARCH ANIMAL RECORD   ")
print("==============================")

#1. Collect inputs from the researcher
rat_id = input("Enter Rat ID (e.g., R005): ")
weight = input("Enter Weight in grams (e.g., 220): ")
group = input("Enter Experimental Group (e.g., Silymarim 100mg): ")
treatment = input("enter Treatment regimen (e.g., silymarin); ")

# Convert weight to an integer so we can do scientific checks on it
weight_num = int(weight)

print("==============================")
print("     RESEARCH SUMMARY         ")
print("==============================")
print(f"Rat ID:    {rat_id}")
print(f"Weight:    {weight_num}g")
print(f"Group:     {group}")
print(f"Treatment: {treatment}")
print("------------------------------")

#2. Apply "MSc Knowledge" check automatically!
#Check A: Monitor pot-surgical weight loss (common in stroke/BCCAO models)
if weight_num < 350:
    print("WARNING: Low body weight (<250g). Monitor closely for post_operative dysphagia or dehydration.")
else:
    print(" Status:Body weight within acceptable physiological parameters")

    # Check B: Check for surgical model monitoring protocols
    if "silymarin 100mg" in group.lower():
        print("WARNING PROTOCOL: Post-BCCAO animal. Monitor neurological deficit scores and check access to softened food.")


