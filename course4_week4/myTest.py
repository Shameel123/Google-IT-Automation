import csv
import requests

url = 'http://marga.com.ar/employees-with-date.csv'

def get_file_lines(url):
    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)

            return row

get_file_lines(url)




