package com.example.user.jj_ras_app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.Charset;

public class readFromStream {
    public String read(HttpURLConnection conn) throws IOException {
        InputStream inputStream = conn.getInputStream();
        StringBuilder output = new StringBuilder();
        if(inputStream != null){
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream, Charset.forName("UTF-8"));
            BufferedReader reader = new BufferedReader(inputStreamReader);
            String line = reader.readLine();
            while(line != null){
                output.append(line);
                line = reader.readLine();
            }
        }
        return output.toString();
    }
    public HttpURLConnection makeHttpRequest(String surl) throws IOException{
        URL url = new URL(surl);
        if (url == null){
            return null;
        }
        HttpURLConnection conn = null;
        try{
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setReadTimeout(10000);
            conn.setConnectTimeout(15000);
            conn.connect();
            if(conn.getResponseCode() != 200) {
                return null;
            }
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            if (conn != null){
                conn.disconnect();
            }
        }
        return conn;
    }
}
