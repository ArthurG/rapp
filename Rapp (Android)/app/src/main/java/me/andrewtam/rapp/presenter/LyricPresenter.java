package me.andrewtam.rapp.presenter;

import android.util.Log;

import javax.inject.Inject;

import me.andrewtam.rapp.RappApplication;
import me.andrewtam.rapp.model.api.pojo.Analytics;
import me.andrewtam.rapp.model.api.pojo.GenerateNewLInes;
import me.andrewtam.rapp.model.api.pojo.LyricResponse;
import me.andrewtam.rapp.model.api.RappClient;
import me.andrewtam.rapp.model.api.pojo.Lyrics;
import me.andrewtam.rapp.view.lyric.LyricView;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LyricPresenter implements Presenter<LyricView> {

    private LyricView view;

    @Inject RappClient client;

    private int id;

    public LyricPresenter(int id) {
        this.id = id;
    }

    public void newLine() {
        Call<GenerateNewLInes> b = client.getNewLine(id);
        b.enqueue(new Callback<GenerateNewLInes>() {
            @Override
            public void onResponse(Call<GenerateNewLInes> call, Response<GenerateNewLInes> response) {
                if(response.isSuccessful()) view.getNextLyric(response.body().getNewlines());
            }

            @Override
            public void onFailure(Call<GenerateNewLInes> call, Throwable t) {
                Log.d("???", t.toString());
            }
        });
    }

    @Override
    public void attachView(LyricView view) {
        RappApplication.getPresenterComponent().inject(this);
        this.view = view;
    }

    @Override
    public void detachView() {
        this.view = null;
    }

    public void loadLyrics() {
        Call<LyricResponse> call = client.getLyrics(id);
        call.enqueue(new Callback<LyricResponse>() {
            @Override
            public void onResponse(Call<LyricResponse> call, Response<LyricResponse> response) {
                if (response.isSuccessful()) view.setView(response.body().getLines());
            }

            @Override
            public void onFailure(Call<LyricResponse> call, Throwable t) {

            }
        });
    }

    public void loadAnalytics() {
        Call<Analytics> call = client.getAnalytics(id);
        call.enqueue(new Callback<Analytics>() {
            @Override
            public void onResponse(Call<Analytics> call, Response<Analytics> response) {
                if (response.isSuccessful()) {
                    Analytics a = response.body();
                    view.setSentiment(a.getSentiment());
                    view.setKeywords(a.getKeywords());
                    view.setSyllable(a.getSyllableArray());
                    view.setRhyme(a.getRhymeWords());
                }
            }

            @Override
            public void onFailure(Call<Analytics> call, Throwable t) {
                Log.d("DER", t.toString());
            }
        });
    }
}
