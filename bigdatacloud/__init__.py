
__author__ = 'Olumide Josiah Akinremi'
__email__ = 'dev@olumidesan.me'
__version__ = '1.0.0'
__license__ = 'MIT'



from requests import Session
from urllib.parse import urlencode

from .utils import validate_args
from .config import MODES_AND_PARAMS, ISO_639_1_CODES


class BigDataCloud:
    """
    Class for interacting with the different APIs BigDataCloud offers.
    Kindly visit https://www.bigdatacloud.com/ for further information
    
    :param: :api_key: API key needed for authorization
    """

    # API Base URL
    API_BASE_URL = 'https://api.bigdatacloud.net/data'
    # Languages BigDataCloud supports
    SUPPORTED_LANGUAGES = list(ISO_639_1_CODES.values())
    
    def __init__(self, api_key:str=''):
        self.api_key = api_key
        self._session = Session()

    def _format_url(self, endpoint:str, values:dict={}):
        """
        Internal function that helps to format the url to the 
        required format before querying the api
        """
        q_params = ''
        
        if bool(values):
            q_params += urlencode(values)
            q_params = f"?{q_params}"

        url = f"{self.API_BASE_URL}/{endpoint}{q_params}"

        return url
    
    def _make_request(self, url):
        """
        Internal function that makes a GET request to the API

        :return: JSON response from the api
        """

        with self._session as s:
            resp = s.get(url)
            resp.raise_for_status()

        return resp.json()        

    def _retrieve_url_params(self, category:str, index:int, *args):
        """
        Extracts url parameters from a given api category and index
        
        :return: (`endpoint` -> str, `qp` -> dict)
        """

        endpoint = list(MODES_AND_PARAMS[category])[index]
        params = MODES_AND_PARAMS[category][endpoint]   

        if 'key' in params:
            values = list(args)
            values.append(self.api_key)
        else:
            values = args

        qp = dict(zip(params, values))

        return endpoint, qp

    @validate_args
    def ip_geolocation(self, *, ip:str='', lang:str='en'):
        """
        Get IP Geolocation data

        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English        
        """

        category = 'ip_geolocation'
        index = 0

        endpoint, params = self._retrieve_url_params(category, index, ip, lang)
        url = self._format_url(endpoint, params)
        
        return self._make_request(url)

    @validate_args
    def ip_geolocation_full(self, *, ip:str='', lang:str='en'):
        """
        Get Full IP Geolocation data

        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English            
        """        

        category = 'ip_geolocation'
        index = 1

        endpoint, params = self._retrieve_url_params(category, index, ip, lang)
        url = self._format_url(endpoint, params)
        
        return self._make_request(url)

    @validate_args
    def ip_geolocation_with_confidence(self, *, ip:str='', lang:str='en'):
        """
        Get IP Geolocation data with confidence

        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English            
        """        

        category = 'ip_geolocation'
        index = 2

        endpoint, params = self._retrieve_url_params(category, index, ip, lang)
        url = self._format_url(endpoint, params)
        
        return self._make_request(url)

    @validate_args
    def reverse_geocode_client(self, *, latitude:str='', longitude:str='', lang:str='en'):
        """
        Get reverse geocode information for client
        
        :param: :latitude: Latitude value as per WGS 84 reference system (GPS system). 
                           Expected values are in [-90, 90] range.
        :param: :longitude: Longitude value as per WGS 84 reference system (GPS system). 
                            Expected values are in [-180, 180] range.
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English    
        """

        index = 0
        category = 'geocoding'

        endpoint, params = self._retrieve_url_params(category, index, latitude, longitude, lang)
        url = self._format_url(endpoint, params)
        
        return self._make_request(url)

    @validate_args
    def reverse_geocode(self, *, latitude:str='', longitude:str='', lang:str='en'):
        """
        Get reverse geocode information
        
        
        :param: :latitude: Latitude value as per WGS 84 reference system (GPS system). 
                           Expected values are in [-90, 90] range.
        :param: :longitude: Longitude value as per WGS 84 reference system (GPS system). 
                            Expected values are in [-180, 180] range.    
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English            
        """        

        index = 1
        category = 'geocoding'

        endpoint, params = self._retrieve_url_params(category, index, latitude, longitude, lang)
        url = self._format_url(endpoint, params)
        
        return self._make_request(url)

    @validate_args
    def client_info(self):
        """Get client information of the initiator of the request to the api"""        

        index = 0
        category = 'client_info'

        endpoint, params = self._retrieve_url_params(category, index)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def am_i_roaming(self, *, latitude:str='', longitude:str=''):
        """
        Get roaming information given a set of coordinates (`latitude` and `longitude`)
        
        :param: :latitude: Latitude value as per WGS 84 reference system (GPS system). 
                           Expected values are in [-90, 90] range.
        :param: :longitude: Longitude value as per WGS 84 reference system (GPS system). 
                            Expected values are in [-180, 180] range.              
        """          

        index = 1
        category = 'client_info'

        endpoint, params = self._retrieve_url_params(category, index, latitude, longitude)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def user_agent_info(self, *, user_agent_raw:str=''):
        """
        Get user agent information of the initiator of the request to the api
        
        :param: :user_agent_raw: User agent string
        """  

        index = 2
        category = 'client_info'

        endpoint, params = self._retrieve_url_params(category, index, user_agent_raw)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def client_ip(self):
        """
        Returns the public IPv4 address of a customer accessing your services. 
        It also offers proxy detection by examining the X-Forwarded-For (XFF) HTTP header field
        """  

        index = 3
        category = 'client_info'

        endpoint, params = self._retrieve_url_params(category, index)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def timezone_by_ip(self, *, ip:str='', utc_reference:int=0):
        """
        Returns detailed active time zone information estimated by IPv4 IP address geolocation, 
        including daylight saving adjustments if applicable. 

        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :utc_reference: UTC time reference in Unix Time Seconds format. 
                                When omitted or invalid, the current time is assumed        
        """  

        index = 0
        category = 'timezone'

        endpoint, params = self._retrieve_url_params(category, index, ip, utc_reference)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args    
    def timezone_info(self, *, timezone_id:str='', utc_reference:int=0):
        """
        Returns detailed active IANA time zone information including daylight saving adjustments 
        if applicable. It will also return the current local time by default, or if supplied with 
        a UTC reference time, it will automatically perform a timezone conversion for you. 

        :param: :timezone_id: Time Zone name in IANA format e.g 'Australia/Sydney'
        :param: :utc_reference: UTC time reference in Unix Time Seconds format. 
                        When omitted or invalid, the current time is assumed
        """          

        index = 1
        category = 'timezone'

        endpoint, params = self._retrieve_url_params(category, index, timezone_id, utc_reference)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def timezone_by_location(self, *, latitude:str='', longitude:str='', utc_reference:int=0):
        """
        Returns detailed active time zone information for the supplied geolocation coordinates,
        including daylight saving adjustments if applicable

        
        :param: :latitude: Latitude value as per WGS 84 reference system (GPS system). 
                           Expected values are in [-90, 90] range.
        :param: :longitude: Longitude value as per WGS 84 reference system (GPS system). 
                            Expected values are in [-180, 180] range.
        :param: :utc_reference: UTC time reference in Unix Time Seconds format. 
                                When omitted or invalid, the current time is assumed
        """  

        index = 2
        category = 'timezone'

        endpoint, params = self._retrieve_url_params(category, index, latitude, longitude, utc_reference)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def country_by_ip(self, *, ip:str='', lang:str='en'):
        """
        Returns detailed information about the country identified by geolocating the provided IPv4 IP address. 
        This includes ISO defined names, languages, currencies, United Nations and Word Bank defined region names and income levels

        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English    
        """

        index = 0
        category = 'country_info'

        endpoint, params = self._retrieve_url_params(category, index, ip, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def country_info(self, *, code:str='', lang:str='en'):
        """
        Returns detailed information about World Countries including ISO defined names, 
        languages and currencies. United Nations and Word Bank defined region name and 
        income level is also provided.

        :param: :code: Default country code, acceptable in:
                       ·       ISO 3166-1 Alpha-2 code
                       .       ISO 3166-1 Alpha-3 code
                       ·       ISO 3166-1 Numeric code
        :param: :lang: Preferred language for locality names in ISO 639-1 format.
        """

        index = 1
        category = 'country_info'

        endpoint, params = self._retrieve_url_params(category, index, code, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def asn_info(self, *, asn:str='', lang:str='en'):
        """
        Returns detailed information about an Autonomous System (AS) when provided with an AS number. 
        The information includes registration, IPv4 address space announcements and ranking.

        :param: :asn: Autonomous System Number as string in ASN format (e.g. '123' or 'AS123' or 'ASN123')
        :param: :lang: Preferred language for locality names in ISO 639-1 format.
        """

        index = 0
        category = 'asn_info'

        endpoint, params = self._retrieve_url_params(category, index, asn, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def asn_info_full(self, *, asn:str='', lang:str='en'):
        """
        Returns extended, detailed information about an Autonomous System (AS) by AS number. 
        The information includes registration, IPv4 address space announcements, ranking, connectivity
        and the most active area data.

        :param: :asn: Autonomous System Number as string in ASN format (e.g. '123' or 'AS123' or 'ASN123')
        :param: :lang: Preferred language for locality names in ISO 639-1 format.   
        """

        index = 1
        category = 'asn_info'

        endpoint, params = self._retrieve_url_params(category, index, asn, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def tor_exit_nodes_list(self, *, batch_size:int=1, offset:int=0, lang:str='en'):
        """
        Returns list of active TOR exit nodes geolocated to country level along with active carrier information

        :param: :batch_size: Requested batch size. Maximum value = 1000
        :param: :offset: Number of entries to skip
        :param: :lang: Preferred language for locality names in ISO 639-1 format.         
        """

        index = 0
        category = 'insights'

        endpoint, params = self._retrieve_url_params(category, index, batch_size, offset, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def address_space_stats_ipv4(self):
        """Returns most recent IPv4 address space registration and BGP """

        index = 1
        category = 'insights'

        endpoint, params = self._retrieve_url_params(category, index)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def network_by_ip(self, *, ip:str='', lang:str='en'):
        """
        Returns detailed information about the active network a specific IP address belongs 
        to, including Autonomous Systems (AS) that announce and serve that network.
        
        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English         
        """

        index = 0
        category = 'network'

        endpoint, params = self._retrieve_url_params(category, index, ip, lang)
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def prefixes_list(self, *, bogons_only:bool=False, batch_size:int=1, offset:int=0, lang:str='en'):
        """
        Returns returns IPv4 address space routes/prefixes

        :param: :bogons_only: Limit to bogon routes only or not. Default (False) – no limit
        :param: :batch_size: Requested batch size. Maximum value = 1000
        :param: :offset: Number of entries to skip
        :param: :lang: Preferred language for locality names in ISO 639-1 format.        
        """

        index = 1
        category = 'network'

        endpoint, params = self._retrieve_url_params(category, index, bogons_only, batch_size, offset, lang) 
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def network_by_cidr(self, *, cidr:str='', depth_limit:int=1,  bogons_only:bool=False, asn:str='', lang:str='en'):
        """
        Returns all the networks that are currently announced on 
        Border Gateway Protocol (BGP) within a specified CIDR

        :param: :cidr: CIDR range in a x.x.x.x/y format. Where x: (0-255), y: (0-32)
        :param: :depth_limit: Defines how many hierarchical levels down to include in the response
        :param: :bogons_only: Limit to bogon routes only or not. Default (False) – no limit
        :param: :asn: Autonomous System Number as string in ASN format (e.g. '123' or 'AS123' or 'ASN123')
        :param: :lang: Preferred language for locality names in ISO 639-1 format.        
        """

        index = 2
        category = 'network'

        endpoint, params = self._retrieve_url_params(category, index, cidr, depth_limit, bogons_only, asn, lang) 
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def phone_number_validate_by_ip(self, *, number:str='', ip:str='', lang:str='en'):
        """
        Returns Global Phone Number Formatting and Validation API 
        including localised formatting and validation based on IP Geolocation results.
        
        :param: :number: Phone number to be validated, passed as a string without spaces or hyphens
        :param: :ip: IPv4 IP address in a string format. If omitted, the caller’s IP address is assumed
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English      
        """

        index = 0
        category = 'phone_number'

        endpoint, params = self._retrieve_url_params(category, index, number, ip, lang) 
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def phone_number_validate(self, *, number:str='', country_code:str='', lang:str='en'):
        """
        Global Phone Number Formatting and Validation API. 
        Requires default country code for localised phone number validation and format.

        :param: :number: Phone number to be validated, passed as a string without spaces or hyphens
        :param: :country_code: Default country code, acceptable in:
                       ·       ISO 3166-1 Alpha-2 code
                       .       ISO 3166-1 Alpha-3 code
                       ·       ISO 3166-1 Numeric code
        :param: :lang: Preferred language for locality names in ISO 639-1 format. Defaults to English          
        """

        index = 1
        category = 'phone_number'

        endpoint, params = self._retrieve_url_params(category, index, number, country_code, lang) 
        url = self._format_url(endpoint, params)

        return self._make_request(url)

    @validate_args
    def email_verify(self, *, email_address:str=''):
        """
        Determines whether the requested email address matches the pattern of a valid email 
        address and where its domain is properly configured for receiving email.

        :param: :email_address: The email address to be verified.
        """
        index = 0
        category = 'email_validation'

        endpoint, params = self._retrieve_url_params(category, index, email_address) 
        url = self._format_url(endpoint, params)

        return self._make_request(url)
    
    def __repr__(self):
        """`eval()`-able string representation"""

        return f"BigDataCloud(api_key='{self.api_key}')"
