
### BigDataCloud Python Wrapper
A [nicer] python wrapper around [BigDataCloud](https://www.bigdatacloud.com/)'s API offerings. Theirs was just unneccesarily weird.

### Requirements
- Python 3.6+
- Pipenv: ```pip install pipenv```

### Setup
`pipenv` manages the entire setup. Simply run, ```pipenv install``` to install the required dependencies, then ```pipenv shell``` to activate the virtual environment where the dependencies have been installed.

### Usage
[BigDataCloud](https://www.bigdatacloud.com/) offers a variety of API listings. You can visit their website to see all.

From the terminal, as a test:

```
>>> from pprint import pprint
>>> from bigdatacloud import BigDataCloud as BDC
>>> client = BDC(api_key='APISecretKey')
```

For example, 

```
>>> pprint(client.country_info(code='ie', lang='en'))
```

...would return:

```
{
    "isoAlpha2": "IE",
    "isoAlpha3": "IRL",
    "m49Code": 372,
    "name": "Ireland",
    "isoName": "Ireland",
    "isoAdminLanguages": [
        {
            "isoAlpha3": "eng",
            "isoAlpha2": "en",
            "isoName": "English",
            "nativeName": "English"
        },
        {
            "isoAlpha3": "gle",
            "isoAlpha2": "ga",
            "isoName": "Irish",
            "nativeName": "Gaeilge"
        }
    ],
    "unRegion": "Europe/Northern Europe",
    "currency": {
        "numericCode": 978,
        "code": "EUR",
        "name": "Euro",
        "minorUnits": 2
    },
    "wbRegion": {
        "id": "ECS",
        "iso2Code": "Z7",
        "value": "Europe & Central Asia"
    },
    "wbIncomeLevel": {
        "id": "HIC",
        "iso2Code": "XD",
        "value": "High income"
    },
    "callingCode": "353",
    "countryFlagEmoji": "🇮🇪"
}
```

Similarly,

```>>> pprint(client.am_i_roaming(latitude='53.349804', longitude='-6.260310'))```

...would return

```
{
    "isRoaming": true
}
```

### Supported Methods
Given a client, ```client```, an instance of the ```BigDataCloud``` class, the following methods are supported, matching all API offerings from BigDataCloud

```
client.ip_geolocation(**kwargs)
client.ip_geolocation_full(**kwargs)
client.ip_geolocation_with_confidence(**kwargs)
client.reverse_geocode_client(**kwargs)
client.reverse_geocode(**kwargs)
client.client_info()
client.am_i_roaming(**kwargs)
client.user_agent_info(**kwargs)
client.client_ip()
client.timezone_by_ip(**kwargs)
client.timezone_info(**kwargs)
client.timezone_by_location(**kwargs)
client.country_by_ip(**kwargs)
client.country_info(**kwargs)
client.asn_info(**kwargs)
client.asn_info_full(**kwargs)
client.tor_exit_nodes_list(**kwargs)
client.address_space_stats_ipv4()
client.network_by_ip(**kwargs)
client.prefixes_list(**kwargs)
client.network_by_cidr(**kwargs)
client.phone_number_validate_by_ip(**kwargs)
client.phone_number_validate(**kwargs)
client.email_verify(**kwargs)
```

### Todo
 - More argument validation
