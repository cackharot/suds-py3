package org;

import jakarta.jws.WebService;
import jakarta.jws.WebMethod;
import java.util.*;

@WebService
public class InfoService {
    @WebMethod
    public String getInfo(String name) {
        return String.format("Info, %s!", name);
    }
}
