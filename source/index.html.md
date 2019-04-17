---
title: EYN API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - python
  - shell

toc_footers:
  - <a href="mailto:sales@eyn.vision">Request a Developer Key</a>

includes:
  - errors
  - demos/demos

search: true
---

# Introduction

Welcome to the EYN Developer API! You can use our API to access EYN's API endpoints, which can get information on enrolments in our database.

We have language bindings in Python! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

# Authentication

> To authorize, use this code:

```python
from warrant_lite import WarrantLite
wl = WarrantLite(username=<username>, password=<password>, 
                 pool_id=<cognito_pool_id>, client_id=<cognito_client_id>, 
                 client_secret=None)
tokens = wl.authenticate_user()
headers = {'Accept': '*/*',
           'Content-Type': 'application/json; charset=UTF-8',
           'Authorization': tokens['AuthenticationResult']['IdToken']}
```

> Make sure to replace `username` and `password` with your AWS Cognito credentials. Replace `<cognito_pool_id>` with `eu-west-2_8ZNdnSazL` and `<cognito_client_id>` with `4sn0g6boc405tspau0lfl0aiba`.

EYN uses AWS Cognito to authenticate users. Request your credentials from [here](mailto:sales@eyn.vision).

ENY also expects a API key to be included in all API requests to the server. EYN API expects a header to all API requests that looks like the following:

`'Accept': '*/*'` <br>
`'Content-Type': 'application/json; charset=UTF-8'` <br>
`'Authorization': <Cognito Id Token>`

<aside class="notice">
You must replace <code>&#60;Cognito Id Token&#62;</code> with the <code>Id Token</code> response when authenticating to AWS Cognito.
</aside>

# Enrolments
## Get Enrolments
```python
import requests
parameters = {'start_time': 0,
              'end_time': 1554389124,
              'eyn_api_key': <your eyn api key>}
headers = {'Accept': '*/*',
           'Content-Type': 'application/json; charset=UTF-8',
           'Authorization': <Cognito Id Token>}

response = requests.get('https://api.eyn-api.com/api/v1/dev/enrolments',
                        params=parameters, headers=headers)
```

```shell
curl "https://api.eyn-api.com/api/v1/dev/enrolments?
    eyn_api_key=<your eyn api key>&
    start_time=<start time>&
    end_time=<end time>" 
    -H "Authorization: <Cognito Id Token>"
```

> The above command returns JSON structured like this:

```json
{"enrolment_ids": [{"enrolment_id": <enrolment_id_1>},
                   {"enrolment_id": <enrolment_id_2>},
                   ...
                   {"enrolment_id": <enrolment_id_n>}]}
```

This endpoint returns a list of enrolment ids.

### HTTP Request

`GET https://api.eyn-api.com/api/v1/dev/enrolments`

### Query Parameters

Parameter | Default | Required | Description
--------- | :-------: | ----------- | -----------
eyn_api_key | - | Required | The ***api_key*** of EYN to access the endpoints.
start_time | 0 | Optional | If ***start_time*** is set, then the response contains all enrolments from this point in time. ***start_time*** should be supplied as a *string* in UTC format in milliseconds.
end_time | request time | Optional | If ***end_time*** is set, then the response contains all enrolments up to this point in time. ***end_time*** should be supplied as a *string* in UTC format in milliseconds.

### Response Parameters

Parameter |  Type |  Description
--------- | :-----------: | -----------
enrolment_id |  uuid | An ***enrolment_id*** uniquely identifies an enrolment. 


## Get Information about a Specific Enrolment

```python
import requests
parameters = {'eyn_api_key': <your eyn api key>}
headers = {'Accept': '*/*',
           'Content-Type': 'application/json; charset=UTF-8',
           'Authorization': <Cognito Id Token>}

response = requests.get('https://api.eyn-api.com/api/v1/dev/enrolments/<enrolment_id>',
                        params=parameters, headers=headers)
```

```shell
curl "https://api.eyn-api.com/api/v1/dev/enrolments/<enrolment_id>?
    eyn_api_key=<your eyn api key>" 
    -H "Authorization: <Cognito Id Token>"
```

> The above command returns JSON structured like this:

```json
{"other_names" : "John",
 "family_name" : "Doe",
 "date_of_birth": "19700101",
 "images" : {
    "link_identity_document_chip_face": <link>, 
    "link_identity_document_image_front": <link>,
    "link_identity_document_image_mrz": <link>,
    "link_user_selfie": <link>},
  "right_to_work_status": "warn",
  "mrz_verified": true, 
  "is_biometric": true}
```
This endpoint returns information about a specific enrolment.

### HTTP Request

`GET https://api.eyn-api.com/api/v1/dev/enrolments/{enrolment_id}`

<aside class="notice">
You must replace <code>{enrolment_id}</code> with a valid enrolment id (e.g. retrieved via <a href="#get-enrolments" style="text-decoration: none"><code>/enrolment</code></a>).
</aside>

### Query Parameters

Parameter | Default | Required | Description
--------- | :-------: | ----------- | -----------
eyn_api_key | - | Required | The ***api_key*** of EYN to access the endpoints.
enrolment_id | - | Required | The ***enrolment_id*** for that specific information is requested. An 'enrolment_id' can be retrieved via <a href="#get-enrolments" style="text-decoration: none"><code>/enrolment</code></a>.

### Response Parameters

Parameter |  Type |  Description
--------- | :-----------: | -----------
other_names | string | The ***other_names*** parameter contains the given names of an enrolee  (including middle names).
family_name | string | The ***family_name*** parameter contains the family name of an enrolee.
date_of_birth | string | The ***date_of_birth*** parameter contains the date of birth of an enrolee. The returned value has a format of yyyymmdd.
images | dict | The ***images*** parameter contains a list of public links to (a) the face of an enrolee extracted from the identity document's chip, (b) the front view of the identity document, (c) the MRZ of the identity document and (d) the selfie of an enrolee. Not all values must be present.
right_to_work_status | string | The ***right_to_work_status*** parameter contains the status if an enrolee is allowed to work in the UK. Possible values are {ok, warn, bad}.
mrz_verified | Boolean | The ***mrz_verified*** parameter asserts if the scanned MRZ code is correct.
is_biometric | Boolean | The ***is_biometric*** parameter asserts if the chip of the identity document has been read successfully.




