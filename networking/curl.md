## Curl

Command line tool that allows transfer of data across network. Supports many protocols including HTTP, HTTPS, FTP, FTPS, POP3, etc. Supports on universal OS.

```
curl --verbose https://example.com        Inspect all details of request and response

curl https://example.com                  GET request (default), returns body of response
curl -X POST http://URL/example.php       POST request
curl https://{one,two,three}.com          Send multiple requests
curl -i https://example.com               Show response headers

curl -d "option=value" -X POST https://example.com    Sending URL-encoded data
curl -d '{"option": "value"}' -H "Content-Type: application/json" -X POST https://example.com
curl -d "@my-file.json" -X POST https://example.com

curl -L https://example.com       Follow automatically to redirect response specified in Location response header

curl -o file.html https://example.com             Save response to a file

curl -u user:pass https://example.com             Provide basic auth

curl -b "oraclelicense=a" https://example.com     Sending cookies

curl -x 192.168.1:8888 https://example.com        Using proxies
```
