# python-geoacumen-city

## Installation

```
pip install python-geoacumen-city
```

## Usage

```
>>> import geoacumen_city
>>> import maxminddb
>>> reader = maxminddb.open_database(geoacumen_city.db_path)
>>> reader.get("1.1.1.1")
{'city': {'names': {'en': 'Sydney'}},
 'continent': {'code': 'OC',
  'geoname_id': 6255151,
  'names': {'de': 'Ozeanien',
   'en': 'Oceania',
   'es': 'Oceanía',
   'fa': 'اقیانوسیه',
   'fr': 'Océanie',
   'ja': 'オセアニア',
   'ko': '오세아니아',
   'pt-BR': 'Oceania',
   'ru': 'Океания',
   'zh-CN': '大洋洲'}},
 'country': {'geoname_id': 2077456,
  'is_in_european_union': False,
  'iso_code': 'AU',
  'names': {'de': 'Australien',
   'en': 'Australia',
   'es': 'Australia',
   'fa': 'استرالیا',
   'fr': 'Australie',
   'ja': 'オーストラリア',
   'ko': '오스트레일리아',
   'pt-BR': 'Austrália',
   'ru': 'Австралия',
   'zh-CN': '澳大利亚'}},
 'location': {'latitude': -33.8688, 'longitude': 151.209},
 'subdivisions': [{'names': {'en': 'New South Wales'}}]}
>>>
```

Note that you must still comply with the requirements of the DB-IP license specified here: https://db-ip.com/db/download/ip-to-city-lite

That is the following:

> You are free to use this IP to City Lite database in your application, provided you give attribution to DB-IP.com for the data.
>
> In the case of a web application, you must include a link back to DB-IP.com on pages that display or use results from the database. You may do it by pasting the HTML code snippet below into your code :
>
> `<a href='https://db-ip.com'>IP Geolocation by DB-IP</a>`