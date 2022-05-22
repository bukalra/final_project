


{
"callForwarding": {
        "always": {
                "enabled": boolean,
                "destination": "phoneNumner",
                "ringReminderEnabled": boolean, ##If true, a brief tone will be played on the person's phone when a call has been forwarded.
                "destinationVoicemailEnabled": boolean
        },
        "busy": {
                "enabled": true,
                "destination": "phoneNumner",
                "destinationVoicemailEnabled": boolean
        },
        "noAnswer": {
                "enabled": boolean,
                "destination": "phoneNumner",
                "numberOfRings": 2,            
                "systemMaxNumberOfRings": 20,  
                "destinationVoicemailEnabled": booolean
        }
},
"businessContinuity": {     ##Call forward unreachable
        "enabled": boolean,
        "destination": "phoneNumner",
        "destinationVoicemailEnabled": boolean
    }
}