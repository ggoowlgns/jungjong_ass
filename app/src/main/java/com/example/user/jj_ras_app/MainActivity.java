package com.example.user.jj_ras_app;

import android.content.ContentValues;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class MainActivity extends AppCompatActivity {

    private TextView tv_outPut;
    private String url = "https://220.67.124.128:8080";
    private String res = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 위젯에 대한 참조
        tv_outPut = (TextView) findViewById(R.id.tv_outPut);

        //AsyncTask를 통해 HttpURLConnection 수행
        NetworkTask networkTask = new NetworkTask();
        networkTask.execute();
    }

    public class NetworkTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected void onPreExecute(){
            super.onPreExecute();
        }


        @Override
        protected Void doInBackground(Void... params){
            try {
                Document doc = Jsoup.connect(url).get();
                Elements tables = doc.select("table.table.table-striped");
                System.out.println("----------------");
                for(Element e: tables){
                    res += e.text().trim();
                }
            } catch (Exception e){
                e.printStackTrace();
            }
            //RequestHttpURLConnection requestHttpURLConnection = new RequestHttpURLConnection();
            //result = requestHttpURLConnection.request(url, values);
            return null;
        }

        @Override
        protected void onPostExecute(Void result){
            tv_outPut.setText(res);
        }
    }
}
