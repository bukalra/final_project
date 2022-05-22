##Voicemail is configured by default for the user
##Users can change those settings by themself

{
    "voicemailEnabled": boolean,
    "notifications": {                  ##Settings for notifications when there are any new voicemails
            "enabled": boolean,
            "destination": "emailAddress"
    },
    "voicemailCallForward": {
            "enabled": boolean
    },
    "voicemailCallForwardBusy": {
            "enabled": boolean,
            "greeting": "DEFAULT/CUSTOM" ##file to be specified
    },
    "voicemailCallForwardNoAnswer": {
            "enabled": boolean,
            "greeting": "DEFAULT/CUSTOM", ##file to be specified
            "numberOfRings": 3            ##Number of rings before an unanswered call will be sent to voicemail. 
    },
    "transferToNumber": {
            "enabled": boolean          ##Settings for voicemail caller to transfer to a different number by pressing zero (0).
    },
    "emailCopyOfMessage": {             ##Settings for sending a copy of new voicemail message audio via email.
            "enabled": boolean,
            "emailId": "emailAddress"
    }
}