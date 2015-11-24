suds-py3
========

Mirror of http://svn.fedorahosted.org/svn/suds/trunk/ supporting Python3 and some fixes.

Overview
---------
The "Suds" web services client is a lightweight soap-based client for python the is licensed under LGPL.

For details, visit:
  * Project site: https://fedorahosted.org/suds/
  * Documentation https://fedorahosted.org/suds/wiki/Documentation


Fixes by Me
===========
1. Applied some changes to make it work with python 3
2. Tested with .NET WCF basicHttpBinding with BasicAuthentication

Examples
========
Examples folder contains sample SOAP services in JAVA, .NET WCF.

There will be only one python client that loads WSDL from `http://localhost:8181/soap/helloservice?wsdl` <- This is served by one of the above services.

RUN Any one of the above services

RUN `python examples/test_client.py` to test whether this package is working properly.

**Running JAVA Soap service**
* `cd examples/java-soap/ && sh run_service.sh`

**Running .NET WCF service**
* `cd examples/NET45_WCF/ && run_service.bat` <- Run this in Visual Studio developer command prompt
