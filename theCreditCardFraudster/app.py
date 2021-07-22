import random

# Return true if given card number is valid
def checkLuhn(cardNo):
    cardNo = str(cardNo)

    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits -1, -1, -1):
        d = ord(cardNo[i]) - ord ('0')

        if (isSecond == True):
            d = d*2

        # We add two digits to handle
        # Cases that make two digits after
        # Doubling

        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


generatedCardNo = []
candidateCardNo = []

# generate missing part of card number
for i in range (1000000):
    generatedCardNo.append(int(f"{i:6}"))

# add unknown card number part to known part
for i in range (len(generatedCardNo)):
    generatedCardNo[i] = int("543210" + str(generatedCardNo[i]) + "1234")

# check generated card numbers
for cardNo in generatedCardNo:
    if cardNo % 123457 == 0 and checkLuhn(cardNo):
        candidateCardNo.append(cardNo)

# show all candidate cart numbers
for i in candidateCardNo:
    print (i,"\n")
