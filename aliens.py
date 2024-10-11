class UnitConverter:
    def __init__(self):
        self.conversions = {
            'length': {'m': 1, 'cm': 100, 'mm': 1000, 'km': 0.001, 'in': 39.37, 'ft': 3.28},
            'weight': {'kg': 1, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'temperature': {'c': 1, 'f': 5/9, 'k': 1/273.15}
        }

    def convert(self, value, from_unit, to_unit, unit_type):
        if unit_type not in self.conversions:
            return "Invalid unit type."

        if from_unit not in self.conversions[unit_type]:
            return f"Invalid from_unit: {from_unit}."

        if to_unit not in self.conversions[unit_type]:
            return f"Invalid to_unit: {to_unit}."

        if unit_type == 'temperature' and from_unit == 'f':
            value = (value - 32) * 5/9

        if unit_type == 'temperature' and to_unit == 'f':
            value = value * 9/5 + 32

        return value * self.conversions[unit_type][from_unit] / self.conversions[unit_type][to_unit]

def main():
    converter = UnitConverter()

    print("Unit Converter")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        unit_type = 'length'
    elif choice == '2':
        unit_type = 'weight'
    elif choice == '3':
        unit_type = 'temperature'
    else:
        print("Invalid choice.")
        return

    value = float(input("Enter value: "))
    from_unit = input("From unit: ").lower()
    to_unit = input("To unit: ").lower()

    result = converter.convert(value, from_unit, to_unit, unit_type)

    if isinstance(result, str):
        print(result)
    else:
        print(f"{value} {from_unit} = {result} {to_unit}")

if __name__ == "__main__":
    main()