import requests ## requests lib is needed to send message

webhook = "your webhook" ## define webhook link

## define message you want to send through webhook
data = {
    "content" : "The content of message you want to send",
    "username" : "Displayname of webhook sending message"
}

message = requests.post(webhook, json = data) ## sending message through webhook link

print(message.status_code) ## printing status code received upon sending request