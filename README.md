# iphits.py-getcountry-logparser-modules
Repo that contains python script for apache log analysis + logparser and getcountry module.

## Access_Log Processing in Python

- logparser.py
  
  - This  module will parse access_log fields and return as dict.

  - #### logline before parsing
  ```
  109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "POST /administrator/index.php HTTP/1.1" 200 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0"
  ```
  - #### logline after parsing
  ```
  {'host': '109.169.248.247', 'identity': '-', 'user': '-', 'time': '12/Dec/2015:18:25:11 +0100', 'request': 'POST /administrator/index.php HTTP/1.1', 'status': '200', 'size': '4494', 'referer': 'http://almhuette-raith.at/administrator/', 'agent': 'Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0'}
  ```

NOTE: Aquiring information about the IP is done through ipstack api call. Please create a free account and create an api token to use it in the script.


## Example of the output from iphits.py script:

```
$  ./iphits.py   access_log 350
   IP           Country       : Hits
########################################
37.1.206.196    Netherlands   : 534
213.150.254.81  Austria       : 434
148.251.50.49   Germany       : 1929
84.112.161.41   Austria       : 712
52.22.118.215   United States : 734
205.167.170.15  United States : 15695
79.142.95.122   Kazakhstan    : 3207
```
