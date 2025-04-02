set1 = set(input("Enter the first set (comma-separated elements): ").strip().split(","))
set2 = set(input("Enter the second set (comma-separated elements): ").strip().split(","))
set3 = set(input("Enter the third set (comma-separated elements): ").strip().split(","))

print(f"\nThe set union is {(set1.union(set2)).union(set3)}")
print(f"The set intersection is {(set1.intersection(set2)).intersection(set3)}")