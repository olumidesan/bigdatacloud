
import pytest

from . import *

from bigdatacloud import BigDataCloud
from requests.exceptions import HTTPError
from bigdatacloud.exceptions import UnsupportedLanguageError, InvalidGeolocationError


bdc_valid = BigDataCloud(api_key=API_KEY)
bdc_invalid = BigDataCloud(api_key="API_KEY")


# Basic Testing with a valid API_KEY: Ensure each type of api call works
def test_ip_geolocation():
    try:
        bdc_valid.ip_geolocation(ip=IP, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_ip_geolocation_full():
    try:
        bdc_valid.ip_geolocation_full(ip=IP, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_ip_geolocation_with_confidence():
    try:
        bdc_valid.ip_geolocation_with_confidence(ip=IP, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

# Requires no valid api key
def test_reverse_geocode_client():
    bdc_valid.reverse_geocode_client(latitude=LATITUDE, longitude=LONGITUDE, lang=LANGUAGE)  

def test_reverse_geocode():
    try:
        bdc_valid.reverse_geocode(latitude=LATITUDE, longitude=LONGITUDE, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

# Requires no valid api key
def test_client_info():
    bdc_valid.client_info()

# Requires no valid api key  
def test_am_i_roaming():
    bdc_valid.am_i_roaming(latitude=LATITUDE, longitude=LONGITUDE)  

def test_user_agent_info():
    try:
        bdc_valid.user_agent_info(user_agent_raw=USER_AGENT)
    except HTTPError:
        pytest.fail()    

# Requires no valid api key
def test_client_ip():
    bdc_valid.client_ip()   

def test_timezone_by_ip():
    try:
        bdc_valid.timezone_by_ip(ip=IP, utc_reference=UTC_REF)
    except HTTPError:
        pytest.fail()    

def test_timezone_by_location():
    try:
        bdc_valid.timezone_by_location(latitude=LATITUDE, longitude=LONGITUDE, utc_reference=UTC_REF)
    except HTTPError:
        pytest.fail()    

def test_timezone_info():
    try:
        bdc_valid.timezone_info(timezone_id=TIMEZONE_ID, utc_reference=UTC_REF)
    except HTTPError:
        pytest.fail()    

def test_country_by_ip():
    try:
        bdc_valid.country_by_ip(ip=IP, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_country_info():
    try:
        bdc_valid.country_info(code=CODE, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_asn_info():
    try:
        bdc_valid.asn_info(asn=ASN, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_asn_info_full():
    try:
        bdc_valid.asn_info_full(asn=ASN, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_tor_exit_nodes_list():
    try:
        bdc_valid.tor_exit_nodes_list(lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

# Requires no valid api key
def test_address_space_stats_ipv4():
    bdc_valid.address_space_stats_ipv4()   

def test_network_by_ip():
    try:
        bdc_valid.network_by_ip(ip=IP, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_prefixes_list():
    try:
        bdc_valid.prefixes_list(lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_network_by_cidr():
    try:
        bdc_valid.network_by_cidr(cidr=CIDR, asn=ASN, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_phone_number_validate_by_ip():
    try:
        bdc_valid.phone_number_validate_by_ip(number=NUMBER, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_phone_number_validate():
    try:
        bdc_valid.phone_number_validate(number=NUMBER, country_code=COUNTRY_CODE, lang=LANGUAGE)
    except HTTPError:
        pytest.fail()    

def test_email_validation():
    try:
        bdc_valid.email_verify(email_address=EMAIL_ADDRESS)
    except HTTPError:
        pytest.fail()    

###########################################################################
# Basic Testing with an *invalid* API_KEY: Ensure each type of api call fails
def test_ip_geolocation_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.ip_geolocation(ip=IP, lang=LANGUAGE)

def test_ip_geolocation_full_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.ip_geolocation_full(ip=IP, lang=LANGUAGE)   

def test_ip_geolocation_with_confidence_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.ip_geolocation_with_confidence(ip=IP, lang=LANGUAGE)   

def test_reverse_geocode_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.reverse_geocode(latitude=LATITUDE, longitude=LONGITUDE, lang=LANGUAGE)   

def test_user_agent_info_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.user_agent_info(user_agent_raw=USER_AGENT)   

def test_timezone_by_ip_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.timezone_by_ip(ip=IP, utc_reference=UTC_REF)   

def test_timezone_by_location_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.timezone_by_location(latitude=LATITUDE, longitude=LONGITUDE, utc_reference=UTC_REF)   

def test_timezone_info_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.timezone_info(timezone_id=TIMEZONE_ID, utc_reference=UTC_REF)

def test_country_by_ip_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.country_by_ip(ip=IP, lang=LANGUAGE)   

def test_country_info_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.country_info(code=CODE, lang=LANGUAGE)   

def test_asn_info_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.asn_info(asn=ASN, lang=LANGUAGE)   

def test_asn_info_full_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.asn_info_full(asn=ASN, lang=LANGUAGE)   

def test_tor_exit_nodes_list_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.tor_exit_nodes_list(lang=LANGUAGE)   

def test_network_by_ip_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.network_by_ip(ip=IP, lang=LANGUAGE)   

def test_prefixes_list_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.prefixes_list(lang=LANGUAGE)   

def test_network_by_cidr_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.network_by_cidr(cidr=CIDR, asn=ASN, lang=LANGUAGE)   

def test_phone_number_validate_by_ip_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.phone_number_validate_by_ip(number=NUMBER, lang=LANGUAGE)   

def test_phone_number_validate_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.phone_number_validate(number=NUMBER, country_code=COUNTRY_CODE, lang=LANGUAGE)   

def test_email_validation_fail():
    with pytest.raises(HTTPError):
        bdc_invalid.email_verify(email_address=EMAIL_ADDRESS)   


################################################################
# Argument validation
def test_email_address_validation():
    with pytest.raises(ValueError):
        bdc_valid.email_verify(email_address='foo@bar')

def test_utc_reference_validation():
    with pytest.raises(ValueError):
        bdc_valid.timezone_by_location(latitude=LATITUDE, longitude=LONGITUDE, utc_reference='MyUTC')

def test_language_validation():
    with pytest.raises(UnsupportedLanguageError):
        bdc_valid.ip_geolocation(ip=IP, lang='yy')

def test_ip_validation():
    with pytest.raises(ValueError):
        bdc_valid.ip_geolocation(ip='192.168', lang=LANGUAGE)

def test_cidr_validation():
    with pytest.raises(ValueError):
        bdc_valid.network_by_cidr(cidr='8.0.0.0/55', asn=ASN)

def test_number_validation():
    with pytest.raises(ValueError):
        bdc_valid.phone_number_validate(number='myphonenumber', country_code=COUNTRY_CODE)

def test_latitude_validation():
    with pytest.raises(InvalidGeolocationError):
        bdc_valid.timezone_by_location(latitude='-350', longitude=LONGITUDE)

def test_longitude_validation():
    with pytest.raises(InvalidGeolocationError):
        bdc_valid.timezone_by_location(latitude=LATITUDE, longitude='95')

def test_representation():
    assert "BigDataCloud(api_key='API_KEY')" == repr(bdc_invalid)        

