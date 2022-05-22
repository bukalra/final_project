from unittest import result
import requests, json
api_token = "NWFkMThjNWMtYmJhYi00YmZkLWFiZDMtNGZhNzc2NjkzMDg2NzYzMDFkNmItZjcy_PE93_0caae1aa-9723-461c-90c6-e1e0b5c9081b"
location_id = "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2ZjMTlhNWM2LTY0ZTQtNGRmYS04Y2Y1LTJmMzdiMWUxOWE3NA"
org_Id="0caae1aa-9723-461c-90c6-e1e0b5c9081b"

def call_api(endpoint, data, method):
    print('we are inside post api')
    headers = {
        "Authorization": f"Bearer {api_token}","Content-Type":"application/json"
    }
    
    if method == 'post':
        response = requests.post(url=endpoint, data=data, headers=headers)
    elif method == 'get':
        response = requests.get(url=endpoint, data=data, headers=headers)

    return response.json()

def post_hunt_groups(todos):
    data_hg= json.dumps(todos.all()["Calling Huntgroups"])
    endpoint = f'https://webexapis.com/v1/telephony/config/locations/{location_id}/huntGroups?orgId={org_Id}'
    return call_api(endpoint, data_hg, method = "post")


def get_agents():
    endpoint = f'https://webexapis.com/v1/people?callingData=true&locationId={location_id}&max=100'
    data=json.dumps({})
    return call_api(endpoint, data, method = 'get')

def get_single_agent(id):
    endpoint = f'https://webexapis.com/v1/people/{id}'
    data=json.dumps({})
    return call_api(endpoint, data, method = 'get')



""" def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    for list in list_to_choose:
        if list_type in list.keys():
            return response.json()
        return get_popular_movies()            
            

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}" """