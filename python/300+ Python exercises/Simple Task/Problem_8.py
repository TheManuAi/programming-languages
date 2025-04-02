set1 = set(input("Enter the first set(comma-separated elements but at the end): ").strip().split(","))
set2 = set(input("Enter the second set(comma-separated elements but at the end): ").strip().split(","))

print(f"\nThe set difference is {set1.difference(set2)}")
print(f"The set symmertric difference is {set1.symmetric_difference(set2)}")