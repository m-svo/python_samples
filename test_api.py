print ("Loading requests, json modules")
import requests
import json
print ("requests, json modules loaded")
print ("Starting program")
api_token = 'a0000a00b00c0000a0bcdef0a0b0c000'
api_token_input = input("Input token (empty for default - 000): ")
if api_token_input :
    api_token = str(api_token_input)
    print ("New token set.")
else :
    print ("Using default token.")
url_main = 'https://webaddress.com?params=api&type=json&oauth_token=' + api_token
url_reserved = 'https://webaddress2.com?params=api&type=json&oauth_token=' + api_token
url_choice = input("If you want to use extra URL press 1 (any other input for main): ")
if url_choice == '1' :
    url_api = url_reserved
    print ("Extra URL set.")
else :
    url_api = url_main
    print ("Using main URL.")
cat_key = input("Input Key (0x123456...): ")
### DEFINING FUNCTIONS ###
def gen_xml():
    xml = '<xml_data> <Key="{}"> </Key> </xml_data>'.format(str(cat_key))
    return xml
### FUNCTIONS DEFINED! ###
r = requests.post(url_api, data=gen_xml(), verify=False)
print ("XML sent.")
print (r)
print (gen_xml())
#reply = json.loads(json.dumps(r.json())) - this was json abuse, convering dictionary to string and back to dictionary
#if we print json.dumps (string) without json.loads (conversion to dictionary), output will be mixed characters, terminal will mix unicode and ? utf ?
try:
    print (r.json())
except ValueError:
    print ('No json reply received. Check http response.')
