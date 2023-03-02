import requests
import http.client
import urllib.parse
import time
import http.cookiejar
import datetime


def get_software():
    url_parts = urllib.parse.urlparse(url)
    connection = http.client.HTTPSConnection(url_parts.netloc)
    connection.request("HEAD", url_parts.path)
    response = connection.getresponse()
    server_software = response.getheader('server')
    print(f"The server software is {server_software}\n\n")

def extract_cookies():
    cookie_jar = http.cookiejar.CookieJar()
    url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    url_opener.open(url)
    for cookie in cookie_jar:
        print('Name:', cookie.name)
        expiration_datetime = datetime.datetime.fromtimestamp(cookie.expires)
        expiration_date_string = expiration_datetime.strftime("%d-%m-%Y %H:%M:%S")
        print('Expires:', expiration_date_string)
        print('\n')
      

def main():

    get_software()
    if 'Set-Cookie' in response.headers:
        extract_cookies()
    else:
        print('The server does not use cookies\n')

if __name__ == '__main__':
    url = input("Please enter the URL: ")
    response = requests.get(url)
    print(response.headers)
    print("\n\n")
    main()
    input("Press ENTER to exit\n")
