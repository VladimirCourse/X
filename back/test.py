from controllers.chat_controller import ChatController


chat = ChatController('abc')
print(chat.interact('I want to fly').__dict__)

# weather = Weather(unit=Unit.CELSIUS)
# location = weather.lookup_by_location('dublin')
# condition = location.condition
# print(condition)

# client = IATACodesClient('c29b7c79-28fd-43e9-8355-44b4ff008e45')

# location = weather.lookup_by_location('dublin')
# forecasts = location.forecast
# for forecast in forecasts:
#     print(forecast.text)
#     print(forecast.date)
#     print(forecast.high)
#     print(forecast.low)


#lights = DataProvider().get_food('Moscow')

# for fl in flights:
#     print(fl.__dict__)