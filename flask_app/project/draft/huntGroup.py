

{
    "name": "huntGroupNAme",
    "phoneNumber": "E.164 number",
    "extension": "extension",
    "firstName": "firstName",
    "lastName": "lastName",
    "callPolicies": {
        "policy": "UNIFORM", ##routing policy for Hunt group can be: CIRCULAR/REGULAR/SIMULTANEOUS/UNIFORM
        "waitingEnabled": boolean,  ##advance when agent is busy then select false
        "noAnswer": {               ##advance when no answer then select false
             "nextAgentEnabled": boolean,
             "nextAgentRings": 5,
             "forwardEnabled": boolean, ##If true, forwards unanswered calls to the destination after the number of rings occurs.
             "numberOfRings": 0,        
             "destinationVoicemailEnabled": false, ##Forwards 
             },
        },
    "agents": [
        {
            "users": "extensions or emails",
            "users": "extensions or emails",
        }   
    ]
}