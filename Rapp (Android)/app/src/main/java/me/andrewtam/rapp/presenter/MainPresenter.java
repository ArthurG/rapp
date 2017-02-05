package me.andrewtam.rapp.presenter;

import android.util.Log;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

import javax.inject.Inject;

import io.realm.Realm;
import me.andrewtam.rapp.RappApplication;
import me.andrewtam.rapp.model.api.pojo.Lyrics;
import me.andrewtam.rapp.model.api.RappClient;
import me.andrewtam.rapp.view.main.MainView;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class MainPresenter implements Presenter<MainView> {
    @Inject
    RappClient client;
    private MainView view;
    private Realm realm;

    private ArrayList<Long> times = new ArrayList<>();

    public MainPresenter(Realm realm) {
        this.realm = realm;
    }

    @Override
    public void attachView(MainView view) {
        RappApplication.getPresenterComponent().inject(this);
        this.view = view;
    }

    @Override
    public void detachView() {
        this.view = null;
    }

    public void incr(Long time) {
        times.add(time);
    }

    public void clearCtr() {
        times.clear();
    }

    public void upload(File file, final String title) {
        times.add(System.currentTimeMillis());
        RequestBody requestFile = RequestBody.create(MediaType.parse("multipart/form-data"), file);
        MultipartBody.Part body = MultipartBody.Part.createFormData("file", file.getName(), requestFile);
//        ArrayList<String> derp = new ArrayList<String>();
//        derp.add("hello, how are you doing?");
//        derp.add("matthew's phone skin sucks");
//        derp.add("hello!");
//        Call<Lyrics> call = client.sendUpdate(2, new UpdatedLyrics(derp));
//        call.enqueue(new Callback<Lyrics>() {
//            @Override
//            public void onResponse(Call<Lyrics> call, LyricResponse<Lyrics> response) {
//                if(response.isSuccessful())
//                    Log.d("DER", "SUCESS");
//            }
//
//            @Override
//            public void onFailure(Call<Lyrics> call, Throwable t) {
//                Log.d("DER", "FUCK");
//            }
//        });
        Call<Lyrics> call = client.sendRapAudio(body, times.toArray(new Long[times.size()]));
        call.enqueue(new Callback<Lyrics>() {
            @Override
            public void onResponse(Call<Lyrics> call, Response<Lyrics> response) {
                if (response.isSuccessful()) {
                    final Lyrics lyric = response.body();

                    realm.beginTransaction();
                    lyric.setTitle(title);
                    lyric.setDate("2017-02-04");
                    realm.copyToRealm(lyric);
                    realm.commitTransaction();

                } else {
                    Log.d("WTF", "WTF?????");
                }
            }

            @Override
            public void onFailure(Call<Lyrics> call, Throwable t) {
                Log.d("der", "WTF: " + t.getMessage());
            }
        });
    }
}
