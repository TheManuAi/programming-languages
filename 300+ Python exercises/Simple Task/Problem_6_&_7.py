set1 = set(input("Enter the first set(comma-separated elements but at the end): ").strip().split(","))
set2 = set(input("Enter the second set(comma-separated elements but at the end): ").strip().split(","))

print(f"\nThe set union is {set1.union(set2)}")
print(f"The set intersection is {set1.intersection(set2)}")