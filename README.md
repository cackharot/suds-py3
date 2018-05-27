suds-py3
========
[![travisci](https://travis-ci.org/cackharot/suds-py3.svg?branch=master)](https://travis-ci.org/cackharot/suds-py3.svg?branch=master)
[![readthedocs](https://readthedocs.org/projects/suds-py3/badge/?version=latest)](https://readthedocs.org/projects/suds-py3/badge/?version=latest)

Suds is a lightweight SOAP python client for consuming Web Services.

Mirror of http://svn.fedorahosted.org/svn/suds/trunk/ supporting Python3 and some fixes.

## Overview

The "Suds" web services client is a lightweight soap-based client for python the is licensed under LGPL.

For details, visit:
  * Project site: https://fedorahosted.org/suds/
  * Documentation https://fedorahosted.org/suds/wiki/Documentation

Since the original library is no longer supported and documentation also disappeared along with it.

A copy of the documentation is hosted at https://suds-py3.readthedocs.io/en/latest/

This is not my original documentation however I have reformatted to sphinx rST style
and updated few parts to keep the code examples clean and working.

Pull requests are welcome for the `docs`.

## Features
* No class generation
* Provides an object API.
* Reads wsdl at runtime for encoding/decoding
* Supports the following SOAP binding styles:
* Document/Literal
* RPC/Literal
* RPC/Encoded
* Provides objectification of WSDL defined:
* Types ''(objects)''
* Enumerations
* Service and type objects provide inspection via ''print''
* Supports unicode
* HTTP authentication
* ''Basic'' WS-Security

## Installation
```
pip3 install suds-py3
```

## Sample usage
```
from suds.client import Client
client = Client('http://localhost:8181/soap/helloservice?wsdl', username='bob', password='catbob')
result = client.service.sayHello('bob')
# result -> "Hello, bob!"
```

### Examples
Examples folder contains sample SOAP services in JAVA, .NET WCF.

Example has a python client that loads WSDL from `http://localhost:8181/soap/helloservice?wsdl` <- This is served by one of the below services.

RUN Any one of the JAVA/.NET WCF services

RUN `python examples/test_client.py` to test whether this package is working properly.

**Running JAVA Soap service**
* `cd examples/java-soap/ && sh run_service.sh`

**Running .NET WCF service**
* `cd examples/NET45_WCF/ && run_service.bat` <- Run this in Visual Studio developer command prompt
