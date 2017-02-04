package me.andrewtam.rapp.view;

import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import java.io.File;
import java.io.IOException;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;
import io.realm.Realm;
import me.andrewtam.rapp.AudioRecorder;
import me.andrewtam.rapp.DividerItemDecoration;
import me.andrewtam.rapp.R;
import me.andrewtam.rapp.model.Rap;
import me.andrewtam.rapp.presenter.MainPresenter;

public class MainActivity extends AppCompatActivity implements MainView {

    @BindView(R.id.recycler) RecyclerView recycler;

    private MainPresenter presenter;
    private AudioRecorder recorder;
    private Realm realm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        setTheme(R.style.AppTheme_NoActionBar);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ButterKnife.bind(this);
        realm = Realm.getDefaultInstance();


        presenter = new MainPresenter();
        presenter.attachView(this);
        recorder = new AudioRecorder("");

        setUpRecyclerView();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        realm.close();
    }

    @OnClick(R.id.record)
    public void record(View v) {
        realm.executeTransactionAsync(new Realm.Transaction() {
            @Override
            public void execute(Realm realm) {
                realm.createObject(Rap.class);
            }
        });

        try {
            recorder.start();
        } catch (IOException e) {
            e.printStackTrace();
        }


        Toast.makeText(this, "Recording Started", Toast.LENGTH_LONG).show();
    }

    @OnClick(R.id.stop)
    public void stop(View v) {
        try {
            recorder.stop();
        } catch (IOException e) {
            e.printStackTrace();
        }

        Toast.makeText(this, "Recording Stopped", Toast.LENGTH_LONG).show();
        MediaPlayer player = new MediaPlayer();

        try {
            player.setDataSource(recorder.path);
            player.prepare();
        } catch (IOException e) {
            e.printStackTrace();
        }

        player.start();

        //final File file = new File(recorder.path);//Environment.getExternalStorageDirectory(), recorder.path);
        //Uri uri = Uri.fromFile(file);
        File auxFile = new File(recorder.path);
        Log.d("DER", recorder.path);
        presenter.upload(auxFile);
    }

    private void setUpRecyclerView() {
        recycler.setLayoutManager(new LinearLayoutManager(this));
        recycler.setAdapter(new MainAdapter(this, realm.where(Rap.class).findAllAsync(), true));
        recycler.setHasFixedSize(true);
        recycler.addItemDecoration(new DividerItemDecoration(this, DividerItemDecoration.VERTICAL_LIST));
    }
}
