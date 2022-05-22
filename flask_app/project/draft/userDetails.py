"""
Usage:
    -creating users if there is no AS synch
    -updating users' settings - changing extensions, displays name etc.
    -applying licenses - mostr common use case
    -rest of the data will be gathered from the Control Hub (locationID, licensesID etc.)
"""

{
    "emails": "emailAddress",
    "extension": "extensionNumber",
    "phoneNumbers": [
        {
        "type": "numberType",
        "value": "E.164_number"
        }
    ],
    "displayName": "displayName",
    "firstName": "firstName",
    "lastName": "lastName",
    "nickname": "nickname"
}
