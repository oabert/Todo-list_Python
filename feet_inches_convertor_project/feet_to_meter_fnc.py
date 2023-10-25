def convert(feet, inches):
    feet_input = float(feet)
    inches_input = float(inches)
    meters = (feet_input + inches_input / 12) * 0.3048
    return round(meters,2)


if __name__ == '__main__':
    convert(12, 23)
