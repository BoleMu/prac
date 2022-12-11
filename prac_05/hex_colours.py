COLOURS = {"Absolute Zero": "#0048ba",
           "Alizarin crimson": "#e32636",
           "Aqua": "#00ffff",
           "Aureolin": "#fdee00",
           "Beige": "#f5f5dc",
           "Blue Green": "#0d98ba",
           "Bole": "#79443b",
           "Bone": "#e3dac9",
           "Brass": "#b5a642",
           "Canary": "#ffff99"}
print(COLOURS)

color_name = input("Enter color name: ").title()

while color_name != "":
    if color_name in COLOURS:
        print(f"{color_name} {COLOURS[color_name]}")

    color_name = input("Enter color name: ").title()

else:
    print()
