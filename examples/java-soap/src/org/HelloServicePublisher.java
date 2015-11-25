package org;

import org.HelloService;

import com.sun.net.httpserver.BasicAuthenticator;
import com.sun.net.httpserver.HttpContext;
import com.sun.net.httpserver.HttpServer;

import javax.xml.ws.Endpoint;
import java.io.IOException;
import java.net.InetSocketAddress;

public class HelloServicePublisher {
    public static void main(String[] args) throws IOException {
        Endpoint endpoint = Endpoint.create(new HelloService());

        HttpServer server = HttpServer.create(new InetSocketAddress("localhost", 8181), 0);
        server.start();

        HttpContext context = server.createContext("/soap/helloservice");

        context.setAuthenticator(new BasicAuthenticator("test") {
            @Override
            public boolean checkCredentials(String username, String pass) {
                return "bob".equals(username) && "catbob".equals(pass);
            }
        });

        printInfo("http:/" + server.getAddress().toString() + context.getPath());

        endpoint.publish(context);
    }

    private static void printInfo(String url) {
        System.out.println(String.format("Starting the service at %s", url));
        System.out.println(String.format("See WSDL at %s?wsdl", url));
    }
}
