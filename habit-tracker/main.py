import requests
from datetime import *





time_now = datetime.now().hour

d = str(date.today())

current_date = d.replace("-", "")



pixela_endpoint = "https://pixe.la/v1/users"


USERNAME = "rabbito"
TOKEN = "KOIj43210dsak312ok"
GRAPH_ID = "graph1"



user_params = {
    "token": "KOIj43210dsak312ok",
    "username": "rabbito",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# Creating the account

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)




# Creating the graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,

}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


def SubmitTime(total_time, date, mode):

    graph_info = {
        "date": date.replace("-",""),
        "quantity": total_time,
    }

    update_info = {
        "quantity": total_time,
    }

    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.replace('-','')}"

    if mode == "update":
        response = requests.put(url=update_endpoint, json=update_info, headers=headers)
    elif mode == "delete":
        response = requests.delete(url=update_endpoint, headers=headers)

    else:
        response = requests.post(f"{graph_endpoint}/graph1", json=graph_info, headers=headers)
    print(response.text)


SubmitTime("2.5","2024-08-07", "update")
