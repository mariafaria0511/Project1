


rain_total = 0.0
wind_total = 0
days_total = 0
true_inputs = True

while true_inputs:
    try:
        rain = float(input("Enter rain and wind: \n "))

        if rain == -1.0:
            true_inputs = False

        else:
            wind = float(input("Enter the wind: \n"))

            rain_total += rain
            wind_total += wind
            days_total += 1

    except ValueError:
            print("Invalid")

if days_total > 0:
    average_rain = rain_total / days_total
    rounded_rain = round(average_rain, 2)

    average_wind = wind_total / days_total

    weather = (average_rain * 10) + average_wind
    rounded_weather = round(average_rain, 2)

print("Average Rain {} inches".format(rounded_rain))
print("Average wind {} mph".format(average_wind))
print("Weather severity for these {} readings is: {}".format(days_total, weather))


