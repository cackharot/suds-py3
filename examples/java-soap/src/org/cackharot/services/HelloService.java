package org.cackharot.services;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class HelloService {
    private String message = new String("Hello, ");

    public void Hello() {}

    @WebMethod
    public String sayHello(String name) {
        return message + name + ".";
    }

    @WebMethod
    public double add(double a, double b) {
        return a + b;
    }
}
