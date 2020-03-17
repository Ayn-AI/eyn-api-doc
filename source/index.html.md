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

# Quickstart

TL;DR? EYN API provides demo files which show how to query the API endpoints. This way you can directly see what EYN API has to offer. Click <a href="#demos">here</a> to go directly to the demos.

Got more time? Continue exploring the API documentation below. In the following, we'll explain every API endpoint, the query and response parameters and give code examples how to query our endpoints and sample responses. As mentioned above, we provide demos which you can run to see how to query the endpoints in more detail. Any more questions --- let us know at <a href="mailto:developers@eyn.vision">developers@eyn.vision</a>.

# Authentication

> To authorize, use this code:

```python
from warrant_lite import WarrantLite
wl = WarrantLite(username=<username>, password=<password>, 
                 pool_id=<cognito_pool_id>, client_id=<cognito_client_id>, 
                 client_secret=None, pool_region="eu-west-2")
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

response = requests.get('https://api.eyn.ninja/api/v1/prod/enrolments',
                        params=parameters, headers=headers)
```

```shell
curl "https://api.eyn.ninja/api/v1/prod/enrolments?
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

`GET https://api.eyn.ninja/api/v1/prod/enrolments`

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

response = requests.get('https://api.eyn.ninja/api/v1/prod/enrolments/<enrolment_id>',
                        params=parameters, headers=headers)
```

```shell
curl "https://api.eyn.ninja/api/v1/prod/enrolments/<enrolment_id>?
    eyn_api_key=<your eyn api key>" 
    -H "Authorization: <Cognito Id Token>"
```

> The above command returns JSON structured like this:

```json
{"other_names" : "John",
 "family_name" : "Doe",
 "date_of_birth": "19700101",
 "nationality": "AUT",
 "document_type": "P",
 "document_expiry_date": "20420101",
 "images" : {
    "link_identity_document_chip_face": <link>, 
    "link_identity_document_image_front": <link>,
    "link_identity_document_image_mrz": <link>,
    "link_user_selfie": <link>},
  "right_to_work_status": "warn",
  "biometric_checks": {
    "face_matching_score": 92.33,
    "face_matching_status": "passed",
    "model_used": "torch"},
  "document_checks": {
    "mrz_check": true, 
    "chip_check": true},
  "BRP_remarks": "JOHN DOE\nYou can work in the UK until 02 January 2025\nDetails\nOn your current visa, you can:\ndo any job except those listed in the conditions below.\nConditions\nYou cannot:\nwork as a doctor or dentist in training\nplay or coach professional sports\nThese conditions are the standard requirements for your visa.",
  "checked_by": "user1@companydomain.com"
  "checked_at: {
    "site_id": "site_id_<number>"
    "site_name":"site_name" }}
```
This endpoint returns information about a specific enrolment.

### HTTP Request

`GET https://api.eyn.ninja/api/v1/prod/enrolments/{enrolment_id}`

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
nationality | string | The ***nationality*** parameter contains the nationality of an enrolee.
document_type | string | The ***document_type*** parameter contains the document type of the identity document.
document_expiry_date | string | The ***document_expiry_date*** parameter contains the expiration date of the enrolee's identity document. The returned value has a format of yyyymmdd.
images | dict | The ***images*** parameter contains a list of public links to (a) the face of an enrolee extracted from the identity document's chip, (b) the front view of the identity document, (c) the MRZ of the identity document and (d) the selfie of an enrolee. Not all values must be present.
right_to_work_status | string | The ***right_to_work_status*** parameter contains the status if an enrolee is allowed to work in the UK. Possible values are {passed, warn, failed}.
biometric_checks | dict | The ***biometric_checks*** parameter contains a list of biometric checks where (a) ***face_matching_score*** parameter represents a confidence value of the face matching between the selfie and the document image,  (b) ***face_matching_status*** parameter represents the status of the face matching (either *passed* or *failed*), and (c) ***model_used*** parameter represents the model that was used to do the face matching.
document_checks | dict | The ***document_checks*** parameter contains a list of boolean document checks where (a) ***mrz_check*** parameter asserts if the scanned MRZ code is correct and (b) ***chip_check*** parameter asserts if the chip of the identity document has been read successfully.
BRP_remarks | string | The ***BRP_remarks*** parameter contains the remarks of a Biometric Recidency Permit queried to, and verified by, the UK Home Office, if applicable, otherwise it defaults to None.
checked_by | string | The ***checked_by*** parameter contains the email address of the user who did the enrolment.
checked_at | dict | The ***checked_at*** parameter contains location information where (a) ***site_id*** parameter is a unique id for the enrolment site, and (b) ***site_name*** parameter is a (changeable) name for the *site*.

### Remarks

<aside class="notice">
In case the <code>/enrolments/{id}</code> endpoint is queried directly after the <code>/identitycheck</code> endpoint, it might be that *BRP_remarks* displays <code>None</code>. This is because the response from the UK Home Office may take a while. In such a case, please re-query after a certain timeout (typically in a range of less than a minute).
</aside>

# Document Checks

## Perform a Document Check
```python
import requests
data = {'image_base64_encoded': <image in base64 encoding>,
        'eyn_ocr_token': <EYN OCR TOKEN>}
response = requests.post('https://api.eyn.ninja/api/v1/prod/documentcheck',
                         json=data)
```

```shell
curl --data "image_base64_encoded=<image in base64 encoding>"
     --data "eyn_ocr_token=<EYN OCR TOKEN>"
     https://api.eyn.ninja/api/v1/prod/documentcheck
```

> The above command returns JSON structured like this:

```json
{ "age": {
    "years": 31,
    "months": 1,
    "days": 19
},
"dob_doe_dn_hash_present": true,
"document_checks": {
    "is_birth_date_valid": true,
    "is_document_expired": false,
    "is_document_number_valid": true,
    "is_expiry_date_valid": true
},
"right_to_work_uk_status": "passed",
"full_mrz_text": "P<GBRUK<SPECIMEN<<ANGELA<ZOE<<<<<<<<<<<<<<<<\n5334013720GBR8812049F2509286<<<<<<<<<<<<<<00",
"mrz_fields": {
    "birth_date": "19881204",
    "birth_date_hash": "9",
    "country": "GBR",
    "document_number": "533401372",
    "document_number_hash": "0",
    "document_type": "P",
    "expiry_date": "20250928",
    "expiry_date_hash": "6",
    "final_hash": "0",
    "name": "ANGELA ZOE",
    "nationality": "GBR",
    "optional_data": "",
    "optional_data_hash": "0",
    "sex": "F",
    "surname": "UK SPECIMEN"
}}
```

This API endpoint processes an identity document and returns:
<ol>
  <li>The text on the document (First Name , Last name, Date of Birth, etc)</li>
  <li>Several document checks like data validation and consistency </li>
  <li>Age </li>
  <li>UK right to work</li>
  <ol>
    <li>Right to work status</li>
    <li>Right to work remarks (For BRPs) (see  <a href="#get-information-about-a-specific-enrolment">Enrolments</a> endpoint)</li>
    <li>Right to work share status (For BRPs) [next version]</li>
    </ol>
</ol>

Identity documents supported:

<ol>
  <li>Passports</li>
  <li>Identity cards</li>
  <li>Biometric residence permits (Visas)</li>
</ol>

### Drag and Drop Testing

Easy testing by uploading images and identity document examples <a href="https://app.eyn.vision/documentcheck">here.</a>

### HTTP Request

`POST https://api.eyn.ninja/api/v1/prod/documentcheck`

### Payload

Parameter | Default | Required | Description
--------- | :-------: | ----------- | -----------
image_base64_encoded | - | Required | The ***image_base64_encoded*** is the image that should be processed in base64 encoding.
eyn_ocr_token | - | Required |  The ***eyn_ocr_token*** is the token supplied by EYN for authentication.

### Response Parameters

Parameter |  Type |  Description
--------- | :-----------: | -----------
age |  - | The ***age*** of the document holder.
years | Integer | The ***years*** indicates the age of the document holder in years.
months | Integer | The ***months*** indicates the age of the document holder in months substracted by the years.
days | Integer | The ***days***  indicates the age of the document holder in days substracted by the months.
dob_doe_dn_hash_present  | Boolean | The ***dob_doe_dn_hash_present*** checks if the date of birth, date of expiry and document number hash of the MRZ is present.
document_checks |  - | The ***document_checks*** performed on the document.
is_birth_date_valid |  Boolean | The ***is_birth_date_valid*** verifies if the birth date of the document holder is valid.
is_document_expired |  Boolean | The ***is_document_expired*** verifies if the document is expired.
is_document_number_valid |  Boolean | The ***is_document_number_valid*** verifies if the document number of the document is valid.
is_expiry_date_valid |  Boolean | The ***is_expiry_date_valid*** verifies if the expiry date of the document holder is valid.
right_to_work_uk_status |  String | The ***right_to_work_status*** indicates the right to work of the document holder in the UK. Possible values are `passed`, `failed` or `passed_with_possible_limitation`.
full_mrz_text  |  String | The ***full_mrz_text*** is the full  MRZ as a string.
mrz_fields |  - | The ***mrz_fields*** are the specific field contained in the MRZ of the document.
birth_date  |  String | The ***birth_date*** is the birth date of the document holder in format YYYYMMDD.
birth_date_hash  |  String | The ***birth_date_hash*** is the hash of the birth date used to verify the validity of the same.
country  |  String | The ***country*** is the issuing country of the document in ISO alpha3 format.
document_number  |  String | The ***document_number*** is the document number of the document.
document_number_hash  |  String | The ***document_number_hash*** is the hash of the document number used to verify the validity of the same.
document_type  |  String | The ***document_type*** is the document type of the document. This could be either P for passports, Ix for ids, or V for visas.
expiry_date  |  String | The ***expiry_date*** is the birth date of the document holder in format YYYYMMDD.  For `French national ID` documents, this field will display an exception string `SEE-BACK-OF-ID`, since those id's do not contain an expiry date.
expiry_date_hash  |  String | The ***expiry_date_hash*** is the hash of the expiry date used to verify the validity of the same.
final_hash  |  String | The ***final_hash*** is the hash over all other validation hashes.
optional_data  |  String | The ***optional_data*** is any optional data containted in the MRZ.
optional_data_hash  |  String | The ***optional_data_hash***  is the hash of the optional data used to verify the validity of the same.
sex  |  String | The ***sex*** is the sex of document holder. This could be either F for female of M for male.
surname  |  String | The ***surname***  is the last name of the document holder.

# Identity Checks

## Perform a Identity Check
```python
import requests
data = {'document_front_base64_encoded': <document front image in base64 encoding>,
        'document_back_base64_encoded': <document back image in base64 encoding>,
        'selfie_base64_encoded': <selfie image in base64 encoding>,
        'eyn_ocr_token': <EYN OCR TOKEN>,
        'enrolment_site_id': <ENROLMENT SITE ID> (Optional)}
response = requests.post('https://api.eyn.ninja/api/v1/prod/identitycheck',
                         json=data)
```

```shell
curl --data "document_front_base64_encoded=<document front image in base64 encoding>"
     --data "document_back_base64_encoded=<document back image in base64 encoding>"
     --data "selfie_base64_encoded=<selfie image in base64 encoding>"
     --data "eyn_ocr_token=<EYN OCR TOKEN>"
     --data "enrolment_site_id"=<ENROLMENT SITE ID> (Optional)
     https://api.eyn.ninja/api/v1/prod/identitycheck
```

> The above command returns JSON structured like this:

```json
{ "face_checks" : {
    "face_matched": True,
    "face_similarity": 90.26
},
"age": {
    "years": 31,
    "months": 1,
    "days": 19
},
"dob_doe_dn_hash_present": true,
"document_checks": {
    "is_birth_date_valid": true,
    "is_document_expired": false,
    "is_document_number_valid": true,
    "is_expiry_date_valid": true
},
"right_to_work_uk_status": "passed",
"full_mrz_text": "P<GBRUK<SPECIMEN<<ANGELA<ZOE<<<<<<<<<<<<<<<<\n5334013720GBR8812049F2509286<<<<<<<<<<<<<<00",
"mrz_fields": {
    "birth_date": "19881204",
    "birth_date_hash": "9",
    "country": "GBR",
    "document_number": "533401372",
    "document_number_hash": "0",
    "document_type": "P",
    "expiry_date": "20250928",
    "expiry_date_hash": "6",
    "final_hash": "0",
    "name": "ANGELA ZOE",
    "nationality": "GBR",
    "optional_data": "",
    "optional_data_hash": "0",
    "sex": "F",
    "surname": "UK SPECIMEN"
},
"session_id": <enrolment_id>
}
```

This API endpoint processes an identity document and a selfie image and returns: 
<ol>
  <li>The text on the document (First Name , Last name, Date of Birth, etc)</li>
  <li>Several document checks like data validation and consistency </li>
  <li>Age </li>
  <li>Face Checks </li>
  <li>UK right to work</li>
  <ol>
    <li>Right to work status</li>
    <li>Right to work remarks (For BRPs) (see  <a href="#get-information-about-a-specific-enrolment">Enrolments</a> endpoint)</li>
    <li>Right to work share status (For BRPs) [next version]</li>
    </ol>
</ol>

Identity documents supported:

<ol>
  <li>Passports</li>
  <li>Identity cards</li>
  <li>Biometric residence permits (Visas)</li>
</ol>

### Testing

Easy testing with our webflow <a href="https://app.eyn.vision/identitycheck">here.</a>
ID check API response usually takes between 15 to 25 seconds.

### HTTP Request

`POST https://api.eyn.ninja/api/v1/prod/identitycheck`

### Payload

Parameter | Default | Required | Description
--------- | :-------: | ----------- | -----------
document_front_base64_encoded | - | Required | The ***document_front_base64_encoded*** is the document front side image that should be processed in base64 encoding.
document_back_base64_encoded | - | Optional | The ***document_back_base64_encoded*** is the document back image (in case of an identity card) that should be processed in base64 encoding.
selfie_base64_encoded | - | Required | The ***selfie_base64_encoded*** is the selfie image that should be processed in base64 encoding.
eyn_ocr_token | - | Required |  The ***eyn_ocr_token*** is the token supplied by EYN for authentication.
enrolment_site_id  | - | Optional |  The ***enrolment_site_id*** is the site id under which the enrolee's information will be stored in EYN's database (if applicable). All company's specific ***enrolment_site_id's*** can be found on the [here](https://app.eyn.vision/admin/sites) (access to EYN's Dashboard is required). 

### Payload Samples

To ensure a successfull API reponse, please upload images of the document which:

<ol>
  <li>Only include the first page </li>
</ol>
  <aside class="success"> **Good examples**
    <br />
    <center>
    <img src="images/passport_good.jpeg" alt="good sample" style="width:300px;"/>
    </center>
 </aside>
 <aside class="warning"> **Bad examples**
    <br />
    <center>
    <img src="images/passport_bad.jpeg" alt="bad sample" style="width:300px;"/>
    </center>
 </aside>
<ol>
  <li value=2>Do not contain glares</li>
</ol>

### Response Parameters

Parameter |  Type |  Description
--------- | :-----------: | -----------
face_checks |  - | The ***face_checks*** performed on the document and selfie image.
face_matched | Boolean | The ***face_matched*** indicates if the face between the document image and the selfie image match.
face_similarity | Double | The ***face_similarity*** indicates the similarity score of the face match.
age |  - | The ***age*** of the document holder.
years | Integer | The ***years*** indicates the age of the document holder in years.
months | Integer | The ***months*** indicates the age of the document holder in months substracted by the years.
days | Integer | The ***days***  indicates the age of the document holder in days substracted by the months.
dob_doe_dn_hash_present  | Boolean | The ***dob_doe_dn_hash_present*** checks if the date of birth, date of expiry and document number hash of the MRZ is present.
document_checks |  - | The ***document_checks*** performed on the document.
is_birth_date_valid |  Boolean | The ***is_birth_date_valid*** verifies if the birth date of the document holder is valid.
is_document_expired |  Boolean | The ***is_document_expired*** verifies if the document is expired.
is_document_number_valid |  Boolean | The ***is_document_number_valid*** verifies if the document number of the document is valid.
is_expiry_date_valid |  Boolean | The ***is_expiry_date_valid*** verifies if the expiry date of the document holder is valid.
right_to_work_uk_status |  String | The ***right_to_work_status*** indicates the right to work of the document holder in the UK. Possible values are `passed`, `failed` or `passed_with_possible_limitation`.
full_mrz_text  |  String | The ***full_mrz_text*** is the full  MRZ as a string.
mrz_fields |  - | The ***mrz_fields*** are the specific field contained in the MRZ of the document.
birth_date  |  String | The ***birth_date*** is the birth date of the document holder in format YYYYMMDD.
birth_date_hash  |  String | The ***birth_date_hash*** is the hash of the birth date used to verify the validity of the same.
country  |  String | The ***country*** is the issuing country of the document in ISO alpha3 format.
document_number  |  String | The ***document_number*** is the document number of the document.
document_number_hash  |  String | The ***document_number_hash*** is the hash of the document number used to verify the validity of the same.
document_type  |  String | The ***document_type*** is the document type of the document. This could be either P for passports, Ix for ids, or V for visas.
expiry_date  |  String | The ***expiry_date*** is the birth date of the document holder in format YYYYMMDD. For `French national ID` documents, this field will display an exception string `SEE-BACK-OF-ID`, since those id's do not contain an expiry date.
expiry_date_hash  |  String | The ***expiry_date_hash*** is the hash of the expiry date used to verify the validity of the same.
final_hash  |  String | The ***final_hash*** is the hash over all other validation hashes.
optional_data  |  String | The ***optional_data*** is any optional data containted in the MRZ.
optional_data_hash  |  String | The ***optional_data_hash***  is the hash of the optional data used to verify the validity of the same.
sex  |  String | The ***sex*** is the sex of document holder. This could be either F for female of M for male.
surname  |  String | The ***surname***  is the last name of the document holder.
session_id  |  uuid | The ***session_id*** uniquely identifies an enrolment. 

