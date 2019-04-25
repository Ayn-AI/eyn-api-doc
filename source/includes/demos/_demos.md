# Demos

The EYN API includes the following demos:

<a href="#demo-get-enrolments" style="text-decoration: none"><code>Demo Get Enrolments</code></a><br>
<a href="#Demo-get-information-about-a-specific-enrolment" style="text-decoration: none"><code>Demo Get Information about a Specific Enrolment</code></a>

Download and follow the quickstart sections to immediately run the demos. For more details, read the demo guides.

## Demo Get Enrolments
### Quickstart

```python
(1)
git clone https://github.com/Ayn-AI/eyn-api-demo
cd eyn-api-demo
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```

You can download the demo file <a href="https://github.com/Ayn-AI/eyn-api-demo/blob/master/demo_get_enrolments.py">demo_get_enrolments.py</a>.
This demo will show you how to query the <a href="#get-enrolments" style="text-decoration: none">Get Enrolments</a> endpoint. 

(1) Run the following commands to deploy the demo (see tabs on the right-hand side).

(2) To execute, run the following command.

```python
(2)
 python demo_get_enrolments.py
```

(3) You shall see a demo response like this.

```python
(3)
enrolment_id :a987259c-bbbb-4b26-926e-b3e6ab64620d
enrolment_id :64897f67-c798-40c6-8ba6-fbf888892b3a
enrolment_id :764a4755-79e5-4678-9b11-268b0136fcb6
enrolment_id :a62749cd-5a5b-4723-a8b4-e18a674489c3
```

(4) Ask <a href="mailto:sales@eyn.vision">EYN</a> for your production <a href="#authentication">credentials</a> and change 
the following lines in <a href="https://github.com/Ayn-AI/eyn-api-demo/blob/master/demo_get_enrolments.py">demo_get_enrolments.py</a>.

```python
(4)
64:    # TODO: Demo parameters - replace with your eyn credentials
65:    username = "demo@api.eyn.ninja"   # replace with your username
66:    password = "Def4ultP4ssw0rd!"     # replace with your password
67:    cognito_pool_id = ""              # replace with your cognito pool id
68:    cognito_client_id = ""            # replace with your cognito client id
```
This will give you access to your production data. Want to know more? The following demo guide will explain the demo step-by-step.

### Demo Guide

```python
(1)
if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Enrolments')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@api.eyn.ninja"   # replace with your username
    password = "Def4ultP4ssw0rd!"     # replace with your password
    cognito_pool_id = ""              # replace with your cognito pool id
    cognito_client_id = ""            # replace with your cognito client id
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
```
(1)
The entry point of the demo is `if __name__ == '__main__':` 

<aside class="notice">
Make sure that you replace <code>username</code>,  <code>password</code>,  <code>cognito_pool_id</code> and  <code>cognito_client_id</code> with the credentials supplied by EYN.
</aside>

```python
(2)
def do_authentication(username, password, cognito_pool_id, cognito_client_id):
    wl = WarrantLite(username=username, password=password,
                     pool_id=cognito_pool_id, client_id=cognito_client_id,
                     client_secret=None, pool_region="eu-west-2")
    tokens = wl.authenticate_user()
    return tokens
```

For every call to EYN's API you have to authenticate to AWS Cognito. In the demo this is done via
`do_authentication(username, password, cognito_pool_id, cognito_client_id)`

(2)
Authentication can be done via `warrant-lite`. (To install run `pip install warrant-lite`.) After successful authentication, warrent-lite returns the authentication tokens.

```python
(3)
req_auth_headers = {'Accept': '*/*',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Authorization': tokens['AuthenticationResult']['IdToken']}
# Now, we can query EYN API to get a list of enrolments
enrolment_ids = get_enrolments(req_auth_headers)
```

(3)
You can create the autorisation headers using the authentication tokens. Then, we can query EYN's API endpoint <a href="#get-enrolments" style="text-decoration: none">/enrolments</a> via `get_enrolments(req_auth_headers)`.

```python
(4)
def get_enrolments(req_auth_headers):
    parameters = {'start_time': 0,
                  'end_time': str(int(datetime.datetime.now().strftime('%s'))*1000),
                  'eyn_api_key': '4f37a768-887f-427c-a784-95a818e60319'}
    response = requests.get('https://api.eyn.ninja/api/v1/dev/enrolments',
                            params=parameters, headers=req_auth_headers)
    body = json.loads(response.content)
    enrolment_ids = body["enrolment_ids"]
    return enrolment_ids
```

(4)
You can use `requests` to query EYN's API. (To install run `pip install requests`.) The following code sends a `GET` request with `start_time = 0` and `end_time = <current_time_stamp>` to retrieve a list of all enrolments.

```python
(5)
# Let's print the list of enrolments that we retrieved
    print('[eyn-api-demo] Results of querying /enrolments')
    for enrolment_id in enrolment_ids:
        print('enrolment_id :' + enrolment_id["enrolment_id"])
```

(5)
Finally, you can use the returned enrolment_ids in your application. (The demo solely prints the retrieved list of enrolment ids.)

## Demo Get Information about a Specific Enrolment
### Quickstart

```python
(1)
git clone https://github.com/Ayn-AI/eyn-api-demo
cd eyn-api-demo
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```

You can download the demo file <a href="https://github.com/Ayn-AI/eyn-api-demo/blob/master/demo_get_specific_enrolment_info.py">demo_get_specific_enrolment_info.py</a>.
This demo will show you how to query the <a href="#get-information-about-a-specific-enrolment" style="text-decoration: none">Get Information about a Specific Enrolment</a> endpoint. 

(1) Run the following commands to deploy the demo:

(2) To execute, run the following command:

```python
(2)
python demo_get_specific_enrolment_info.py
```

(3) You shall see a demo response like this:

```python
(3)
other_names: MOHAMED
family_name: BEN ARBIA
date_of_birth: 19910205
link_identity_document_chip_face: <link>
link_identity_document_image_front: <link>
link_identity_document_image_mrz: <link>
link_user_selfie: <link>
right_to_work_status: warn
mrz_verified: True
is_biometric: False
```

(4) Ask <a href="mailto:sales@eyn.vision">EYN</a> for your production <a href="#authentication">credentials</a> and change 
the following lines in <a href="https://github.com/Ayn-AI/eyn-api-demo/blob/master/demo_get_specific_enrolment_info.py">demo_get_specific_enrolment_info.py</a>: 

```python
(4)
64:    # TODO: Demo parameters - replace with your eyn credentials
65:    username = "demo@api.eyn.ninja"   # replace with your username
66:    password = "Def4ultP4ssw0rd!"     # replace with your password
67:    cognito_pool_id = ""              # replace with your cognito pool id
68:    cognito_client_id = ""            # replace with your cognito client id
```
This will give you access to your production data. Want to know more? The following demo guide will explain the demo step-by-step.

### Demo Guide

```python
(1)
if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Enrolments')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@api.eyn.ninja"   # replace with your username
    password = "Def4ultP4ssw0rd!"     # replace with your password
    cognito_pool_id = ""              # replace with your cognito pool id
    cognito_client_id = ""            # replace with your cognito client id
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
```

(1) The entry point of the demo is `if __name__ == '__main__':`

<aside class="notice">
Make sure that you replace <code>username</code>,  <code>password</code>,  <code>cognito_pool_id</code> and  <code>cognito_client_id</code> with the credentials supplied by EYN.
</aside>

```python
(2)
def do_authentication(username, password, cognito_pool_id, cognito_client_id):
    wl = WarrantLite(username=username, password=password,
                     pool_id=cognito_pool_id, client_id=cognito_client_id,
                     client_secret=None, pool_region="eu-west-2")
    tokens = wl.authenticate_user()
    return tokens
```

For every call to EYN's API you have to authenticate to AWS Cognito. In the demo this is done via
`do_authentication(username, password, cognito_pool_id, cognito_client_id)`

(2) Authentication can be done via `warrant-lite`. (To install run `pip install warrant-lite`.) After successful authentication, warrent-lite returns the authentication tokens.

```python
(3)
req_auth_headers = {'Accept': '*/*',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Authorization': tokens['AuthenticationResult']['IdToken']}
# Now, we can query EYN API to get specific information about an enrolment
enrolment_info = get_specific_enrolment_info(req_auth_headers, 'd7bd8751-ea88-4e82-94d8-4940cc07eea8')
```

(3) You can create the autorisation headers using the authentication tokens. Then, we can query EYN's API endpoint <a href="#get-information-about-a-specific-enrolment" style="text-decoration: none">/enrolments/{id}</a> via `get_specific_enrolment_info(req_auth_headers, 'd7bd8751-ea88-4e82-94d8-4940cc07eea8')`.

<aside class="notice">
Replace <code>enrolment_id</code> with a valid enrolment id (for example, retrieved via <a href="#get-enrolments" style="text-decoration: none">/enrolments</a>).
</aside>

```python
(4)
def get_specific_enrolment_info(req_auth_headers, enrolment_id):
    parameters = {'eyn_api_key': '4f37a768-887f-427c-a784-95a818e60319'}
    response = requests.get('https://api.eyn.ninja/api/v1/dev/enrolments' + enrolment_id,
                            params=parameters, headers=req_auth_headers)
    enrolment_info = json.loads(response.content)
    return enrolment_info
```

(4) You can use `requests` to query EYN's API. (To install run `pip install requests`.) The following code sends a `GET` request with `enrolment_id = <a valid enrolment id>` to retrieve specific information about that enrolment.

```python
(5)
# Let's print the information that we retrieved
print('[eyn-api-demo] Results of querying /enrolments/d7bd8751-ea88-4e82-94d8-4940cc07eea8:')
print('other_names: ' + enrolment_info["other_names"])
print('family_name: ' + enrolment_info["family_name"])
print('date_of_birth: ' + enrolment_info["date_of_birth"])
if "link_identity_document_chip_face" in enrolment_info["images"]:
    print('link_identity_document_chip_face: ' + enrolment_info["images"]["link_identity_document_chip_face"])
if "link_identity_document_image_front" in enrolment_info["images"]:
    print('link_identity_document_image_front: ' + enrolment_info["images"]["link_identity_document_image_front"])
if "link_identity_document_image_mrz" in enrolment_info["images"]:
    print('link_identity_document_image_mrz: ' + enrolment_info["images"]["link_identity_document_image_mrz"])
if "link_user_selfie" in enrolment_info["images"]:
    print('link_user_selfie: ' + enrolment_info["images"]["link_user_selfie"])
print('right_to_work_status: ' + enrolment_info["right_to_work_status"])
print('mrz_verified: ' + str(enrolment_info["mrz_verified"]))
print('is_biometric: ' + str(enrolment_info["is_biometric"]))
```

(5) Finally, you can use the returned enrolment information in your application. (The demo solely prints all retrieved information.)


