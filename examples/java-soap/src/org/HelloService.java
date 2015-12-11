package org;

import javax.jws.WebMethod;
import javax.jws.WebService;
import java.util.*;

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

    @WebMethod
    public Date addDate(Date inputDate, int days) {
      Calendar c = Calendar.getInstance();
      c.setTime(inputDate);
      c.add(Calendar.DATE, days);
      Date dt = c.getTime();
      return dt;
    }
}
