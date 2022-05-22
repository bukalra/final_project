from flask import request

def hunt_group_form_parser(form, form2, form3a, form3b):

    #parsujemy rzeczy wpisane w fomularzu o tym samym kluczu - tutaj "id"
    agents_chosen = request.form.getlist("id")
    #zamieniamy liste na "set" - to taka lista bez powtorzen.
    agents_chosen_tuple = set(agents_chosen)
    #przydotowujemy list agentow do wpisannia do jsona
    agents_to_write = [{'id':id, 'weight':50} for id in agents_chosen_tuple]   

    hunt_group_json_ready = {
        "name": form.data['name'],
        "phoneNumber": form.data['phoneNumber'],
        "extension": form.data['extension'],
        "languagecode": form.data['languagecode'],
        "firstName": form.data['firstName'],
        "lastName": form.data['lastName'],
        "timezone": form.data['timezone'],
        "callPolicies": {
            "policy": form2.data['policy'],
            "waitingEnabled": form2.data['waitingEnabled'],
            "noAnswer": {
                "nextAgentEnabled": form3a.data['nextAgentEnabled'],
                "nextAgentRings": form3a.data['nextAgentRings'],
                "forwardEnabled": form3a.data['forwardEnabled'],
                "numberOfRings": form3a.data['numberOfRings'],
                "destination": form3a.data['destination'],
                "destinationVoicemailEnabled": form3a.data['destinationVoicemailEnabled']
                },
            "businessContinuity": {
                "enabled": form3b.data['enabled'],
                "destination": form3b.data['destination'],
                "destinationVoicemailEnabled": form3b.data['destinationVoicemailEnabled']
                }
        },
        "agents": agents_to_write,
        "enabled": form.data['enabled']
        }
    return hunt_group_json_ready