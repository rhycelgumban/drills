from visitors import add_visitor

visitors = []

while True:
    add_visitor(visitors)

    again = input("Add another visitor? (yes/no): ").lower()

    if again != "yes":
        break

print("\nBarangay Visitor Log")
print("-" * 30)

for i, visitor in enumerate(visitors, start=1):
    print(f"{i}. {visitor['name']} - {visitor['purpose']}")

print(f"\nTotal visitors recorded: {len(visitors)}")