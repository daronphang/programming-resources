## SOAP Message Body

SOAP message is composed of:

- An envelope tag that begins and ends every message
- A body containing the request and response
- A header if a message must determine any specifics or extra requirements
- A fault informing of any errors that can occur throughout the request processing

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/1999/XMLSchema">
    <SOAP-ENV:Body>
        <ns1:getAddressFromNameResponse xmlns:ns1="urn:www-oracle-com:AddressBook"
            SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
            <return xmlns:ns2="urn:xml-soap-address-demo" xsi:type="ns2:address">
                <city xsi:type="xsd:string">Anytown
                </city>
                <state xsi:type="xsd:string">NY
                </state>
                <phoneNumber xsi:type="ns2:phone">
                    <areaCode xsi:type="xsd:int">123
                    </areaCode>
                    <number xsi:type="xsd:string">7890
                    </number>
                    <exchange xsi:type="xsd:string">456
                    </exchange>
                </phoneNumber>
                <streetName xsi:type="xsd:string">Main Street
                </streetName>
                <zip xsi:type="xsd:int">12345</zip>
                <streetNum xsi:type="xsd:int">123
                </streetNum>
            </return>
        </ns1:getAddressFromNameResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```
