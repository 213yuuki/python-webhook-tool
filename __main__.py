import requests
import os
from time import sleep

webhook = input("Provide discord webhook: ")

webhookOk = requests.request("GET", webhook)
if (webhookOk.status_code == 200):
    os.system('cls')
else:
    os.system('cls')
    print("Provided webhook link is invalid. Error Code: " + str(webhookOk.status_code))
    sleep(1)
    webhook = input("Provide correct discord webhook: ")

try:
    print("1) Spam messages")
    print("2) Delete webhook")
    print("")
    selectOpt = int(input("Select option: "))

    if selectOpt == 1:
        os.system('cls')
        sleep(1)
        msgAmount = input("Number of messages to send (inf for infinite): ")
        msgAuthor = input("Name of the webhook to send as: ")
        msgContent = input("Message content: ")

        data = {
            "content" : msgContent,
            "username" : msgAuthor
        }

        if msgAmount == "inf":
            while True:
                result = requests.post(webhook, json = data)
                if (result.status_code == 204):
                    print("Message sent succesfully")
                else:
                    print("Error: " + str(result.status_code))
        else:
            if msgAmount.isdigit():
                msgAmountInt = int(msgAmount)
                for i in range(msgAmountInt):
                    if i < msgAmountInt:
                        result = requests.post(webhook, json = data)
                        if (result.status_code == 204):
                            print("Message sent succesfully")
                        else:
                            print("Error: " + str(result.status_code))
            else:
                print("Unknown value.")

    elif selectOpt == 2:
        os.system('cls')
        sleep(1)
        delResponse = requests.request("DELETE", webhook)
        if (delResponse.ok):
            print("Deleted webhook")
        else:
            print("Can't delete webhook.")
            print("Error code: " + str(delResponse.status_code))

    else:
        print(selectOpt)

except ValueError:
    print("Something went wrong.")