
This software is implemented based on OpenAPI generator project to operate NWDAF server. Through the python flask, the NWDAF server is implemented based on Python language. 

The NWDAF server operate based on TS 29.520. Also the NWDAF server consists of a Communication module and a Processing module. Communication module, which is created with Python Flask, is responsible for exchanging hyper text transfer protocol (HTTP) messages with service consumers. In Processing module, Controllers identify the uniform resource identifier (URI) of HTTP requests and Models have several functions that can make a decision of what information should be returned.

