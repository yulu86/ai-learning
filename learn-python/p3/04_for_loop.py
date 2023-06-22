successful = False
for number in range(1, 4):
    print("Sending a message:", number, number * ".")
    if successful:
        print("Successful")
        break
else:
    print("Sent 3 times, but failed")
