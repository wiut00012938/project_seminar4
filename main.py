# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def encode(message):
encoded_message = ""
i = 0



# Press the green button in the gutter to run the script.
while (i <= len(message) - 1):
count = 1
char = message[i_of_external]
j = i
while (j < len(message) - 1):
if (message[j] == message[j + 1]):
count = count + 1
j = j + 1
else:
break
encoded_message = encoded_message + str(count) + ch
i = j + 1
return encoded_message
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
