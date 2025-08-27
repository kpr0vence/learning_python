# Add names to a list, access each one and print it
names = ["Reese", "Esca", "Ajax", "Ren", "Gwen"]

print("Accessing names by element:")
for name in names:
    print(f"{name} ", end="" )

print("\n\nAccessing names by index:")
for i in range(len(names)):
    print(f"Name[{i}] = {names[i]}")