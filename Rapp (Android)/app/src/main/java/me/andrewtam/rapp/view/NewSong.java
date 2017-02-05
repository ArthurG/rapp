package me.andrewtam.rapp.view;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.webkit.WebView;

import butterknife.BindView;
import butterknife.ButterKnife;
import me.andrewtam.rapp.R;

/**
 * Created by andrewtam on 2017-02-05.
 */

public class NewSong extends AppCompatActivity {
    @BindView(R.id.webview)
    WebView webView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.play_video);

        ButterKnife.bind(this);
        webView.loadUrl("http://69412307.ngrok.io/songs/56/hello my name is john");
    }
}
