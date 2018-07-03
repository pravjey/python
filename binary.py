import sl4a
from android import Android

droid = sl4a.Android()

# Functions

def binary(num):
    num = int (num)
    remainder = ''
    while num > 0:
        remainder = remainder + str(num % 2)
        num = num // 2
    remainder = reverseString(remainder)
    return remainder
        
def denary(num):
    p = len(num)
    bin2dec = 0
    for i in range (0,p):
        z = int(str (num[p-i-1]))
        bin2dec = bin2dec + (z * (2**i))
    bin2dec = str (bin2dec)
    return bin2dec 

def reverseString(string):
   i = len (string) - 1
   a = ''
   while i >= 0:
       a = a + str (string [i])
       i = i - 1
   return a

def sayBinary (answer):
    i = 0
    while i <= (len (answer) - 1):
        droid.ttsSpeak (str (answer[i]))
        i += 1

def convert(numToConvert, text):
    if 'binary' in text:
        answer = binary (numToConvert)
    elif 'denary' in text:
        answer = denary (numToConvert)
    return answer

def toggleSound(sound):
    if sound == 'on':
        sound = 'off'
    else:
        sound = 'on'
    return sound, 'sound ' + sound


# Methods for input and output

def menu (title,optionslist):
    droid.dialogCreateAlert  (title)
    droid.dialogSetItems (optionslist)
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    return response

def message (x):
    droid.dialogCreateAlert  (x)
    droid.dialogSetNeutralButtonText  ('OK')
    droid.dialogShow()
    response = droid.dialogGetResponse().result

def getInput(choice):
    if choice == 0:
        numToConvert = droid.dialogGetInput ('Enter a denary number').result
        text = "binary"
    elif choice == 1:
        numToConvert = droid.dialogGetInput ('Enter a binary number').result
        text = "denary"
    answer = convert (numToConvert, text)   
    return [numToConvert, text, answer]

def speakOutput (response, output):
    if response == 0:
        droid.ttsSpeak  (output [0] + output [1])
        sayBinary (output [2])
    elif response == 1:
        sayBinary (output [0])
        droid.ttsSpeak  (output [1] + output [2])


# Program
   
def main ():
    message ('Binary - Denary Convertor')
    finished = False
    sound = 'off'
    while not finished:
        response = menu ('Menu', ['Denary to Binary', 'Binary to Denary', 'Sound On/Off', 'Exit'])    
        if response ["item"] == 0 or response ["item"] == 1:
            output = getInput(response["item"])
            response2 = menu (output[0] + " in " + output[1] + " is " + output[2], ["Return to menu", "Exit"])
            if sound == 'on':
                speakOutput (response ["item"], output)
            if response2["item"] == 1:
                finished = True
        elif response ["item"] == 2:
            sound, text = toggleSound(sound)
            droid.makeToast  (text)
            if sound == 'on':
                droid.ttsSpeak (text)
        else:
            finished = True


main()
