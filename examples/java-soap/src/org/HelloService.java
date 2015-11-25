package org;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public class HelloService {
    @WebMethod
    public String sayHello(String name) {
        return String.format("Hello, %s!", name);
    }

    @WebMethod
    public double add(double a, double b) {
        return a + b;
    }
}
