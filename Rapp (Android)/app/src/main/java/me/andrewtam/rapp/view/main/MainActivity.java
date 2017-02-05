package me.andrewtam.rapp.view.main;

import android.content.DialogInterface;
import android.content.Intent;
import android.media.MediaPlayer;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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
import me.andrewtam.rapp.model.api.pojo.Lyrics;
import me.andrewtam.rapp.presenter.MainPresenter;
import me.andrewtam.rapp.view.NewSong;

public class MainActivity extends AppCompatActivity implements MainView {

    @BindView(R.id.recycler) RecyclerView recycler;
    @BindView(R.id.record) Button record;
    @BindView(R.id.space) Button space;
    @BindView(R.id.stop) Button stop;

    private MainPresenter presenter;
    private AudioRecorder recorder;
    private Realm realm;

    private String title;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        setTheme(R.style.AppTheme_NoActionBar);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ButterKnife.bind(this);
        realm = Realm.getDefaultInstance();

        stop.setEnabled(false);
        space.setEnabled(false);
        presenter = new MainPresenter(realm);
        presenter.attachView(this);
        recorder = new AudioRecorder("");

        setUpRecyclerView();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        presenter.detachView();
        realm.close();
    }

    @OnClick(R.id.record)
    public void record(View v) {
        presenter.incr(System.currentTimeMillis());
        try {
            recorder.start();
        } catch (IOException e) {
            e.printStackTrace();
        }

        record.setEnabled(false);
        space.setEnabled(true);
        stop.setEnabled(true);
        Toast.makeText(this, "Recording Started", Toast.LENGTH_LONG).show();
    }

    @OnClick(R.id.space)
    public void incrSpace(View v) {
        presenter.incr(System.currentTimeMillis());
    }

    @OnClick(R.id.stop)
    public void stop(View v) {
        presenter.incr(System.currentTimeMillis());
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

        AlertDialog.Builder dialogBuilder = new AlertDialog.Builder(this);
        LayoutInflater inflater = this.getLayoutInflater();
        final View dialogView = inflater.inflate(R.layout.custom_dialog, null);
        dialogBuilder.setView(dialogView);

        final EditText edt = (EditText) dialogView.findViewById(R.id.edit1);

        dialogBuilder.setTitle("Rap Title");
        dialogBuilder.setMessage("Enter Rap Title below.");
        dialogBuilder.setPositiveButton("Done", new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialog, int whichButton) {
                title = edt.getText().toString();
                File auxFile = new File(recorder.path);
                presenter.upload(auxFile, title);
//                Intent i = new Intent(getApplicationContext(), NewSong.class);
//                startActivity(i);
                //do something with edt.getText().toString();
            }
        });
        AlertDialog b = dialogBuilder.create();
        b.show();

        player.start();
        record.setEnabled(true);
        space.setEnabled(false);
        stop.setEnabled(false);
        Log.d("DER", recorder.path);
        presenter.clearCtr();
    }

    private void setUpRecyclerView() {
        recycler.setLayoutManager(new LinearLayoutManager(this));
        recycler.setAdapter(new MainAdapter(this, realm.where(Lyrics.class).findAllAsync(), true));
        recycler.setHasFixedSize(true);
        recycler.addItemDecoration(new DividerItemDecoration(this, DividerItemDecoration.VERTICAL_LIST));
    }
}
