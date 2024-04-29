temperature= int(input("enter the temperature:"))
print("temp: "+ str(temperature))
temp_unit= input(" type 1 for fehrenheit to centigrade or type 2 for centigrade to fehrenheit: ")
if temp_unit == "1":
    print("when converted to centigrade: "+ str(temperature*33.8))

elif temp_unit =="2":
    print("when converted to fahrenheit: "+ str(temperature/33.8))
else:
    print("invalid input")

