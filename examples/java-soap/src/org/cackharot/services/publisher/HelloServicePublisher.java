package org.cackharot.services.publisher;

import org.cackharot.services.HelloService;

import javax.xml.ws.Endpoint;

public class HelloServicePublisher {
    public static void main(String[] args) {
      final String url = "http://localhost:8181/soap/helloservice";
      System.out.println(String.format("Starting the service at %s", url));
      System.out.println(String.format("See WSDL at %s?wsdl", url));
      Endpoint.publish(url, new HelloService());
    }
}
