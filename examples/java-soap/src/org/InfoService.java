package org;

import javax.jws.WebMethod;
import javax.jws.WebService;
import java.util.*;

@WebService
public class InfoService {
    @WebMethod
    public String getInfo(String name) {
        return String.format("Info, %s!", name);
    }
}
