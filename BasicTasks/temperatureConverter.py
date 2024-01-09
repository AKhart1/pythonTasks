def temperatureConverter():
    temperature = int(input("Enter the temperature: "))
    user_input = input("Enter the scale of temperature: ")

    match user_input:
        case "Fahrenheit":
            print((temperature * 9/5) + 32)
        case "Celsius":
            print((temperature - 32) * 5/9)

temperatureConverter()