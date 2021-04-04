#! usr/bin/python3
"""
Learning Python Requests Module by completing the user guide on https://requests.readthedocs.io/en/latest/

Utilizing https://httpbin.org to test and learn!

As each item in the quickstart is learned, they will be turned in a function to aid in making execution of each item easy and organized.

"""

# Quickstart
import requests

ROOT_URL = 'https://httpbin.org/'
TIMEOUT = 1 # Seconds
PAYLOAD = {}
REQ = "get"

def Make_a_Request():
    r_delete = requests.delete('{}delete'.format(ROOT_URL))
    r_get = requests.get('{}get'.format(ROOT_URL))
    r_patch = requests.patch('{}patch'.format(ROOT_URL))
    r_post = requests.post('{}post'.format(ROOT_URL))
    r_put = requests.put('{}put'.format(ROOT_URL))
    return [r_delete, r_get, r_patch, r_post, r_put]

def Passing_Parameters_In_URLs():
    PAYLOAD = {'key1':'value1', 'key2':'value2', 'key3': ['value3_1','value3_2']}
    r = requests.get('{}{}'.format(ROOT_URL, REQ), params=PAYLOAD)
    print(r.url)
    print(r.status_code,r.reason)


def Response_Content():
    r_delete = Make_a_Request()[0]
    print(r_delete.text) # check for encoding here first
    print("Encoding: {}".format(r_delete.encoding))
    print(type(r_delete.text)) # returns str

# Binary Response Content

def JSON_Response_Content():
    print(r_delete.json())
    print(type(r_delete.json())) # returns dict

# JSON Response Content
print(r_delete.json())
print(type(r_delete.json())) # returns dict

# Raw Response Content
# Custom Headers
# More complicated POST requests
# POST a Multipart-Encoded File

def Response_Status_Codes():
    info_responses = [100, 101, 102, 103]
    successful_responses = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
    client_error_responses = [400, 401, 402, 403]
    for status_code in successful_responses:
        try:
            r = requests.get('{}status/{}'.format(ROOT_URL, status_code), timeout=TIMEOUT)
        except:
            print("TIMEOUT on status_code: {}".format(status_code))
            continue
        print("status_code {}: {}, {}".format(r.status_code, r.url, r.reason))

# Response Headers
# Cookies
# Redirection and History
# Timeouts
# Errors and Exceptions
# Advanced Usage
# Session Objects
# Request and Response Objects
# Prepared Requests
# SSL Cert Verification
# Client Side Certificates
# CA Certificates
# Body Content Workflow
# Keep-Alive
# Streaming Uploads
# Chunk-Encoded Requests
# POST Multiple Multipart-Encoded Files
# Event Hooks
# Custom Authentication
# Streaming Requests
# Proxies
# Compliance
# HTTP Verbs
# Custom Verbs
# Link Headers
# Transport Adapters
# Blocking Or Non-Blocking?
# Header Ordering
# Timeouts
# Authentication
# Basic Authentication
# Digest Authentication
# OAuth 1 Authentication
# OAuth 2 and OpenID Connect Authentication
# Other Authentication
# New Forms of Authentication


"""
dir of requests.get  object:
apparent_encoding
close
connection
content
cookies
elapsed
encoding
headers
history
is_permanent_redirect
is_redirect
iter_content
iter_lines
json
links
next
ok
raise_for_status
raw
reason
request
status_code
text
url



"""