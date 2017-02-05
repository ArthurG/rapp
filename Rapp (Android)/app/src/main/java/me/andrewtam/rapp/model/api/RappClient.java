package me.andrewtam.rapp.model.api;

import me.andrewtam.rapp.model.api.pojo.Analytics;
import me.andrewtam.rapp.model.api.pojo.GenerateNewLInes;
import me.andrewtam.rapp.model.api.pojo.LyricResponse;
import me.andrewtam.rapp.model.api.pojo.Lyrics;
import me.andrewtam.rapp.model.UpdatedLyrics;
import okhttp3.MultipartBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Path;

public interface RappClient {

    @Multipart
    @POST("newsong")
    Call<Lyrics> sendRapAudio(@Part MultipartBody.Part file, @Part("times") Long[] times);

    @POST("songs/{id}")
    Call<Lyrics> sendUpdate(@Path("id") int id, @Body UpdatedLyrics updated_Lyrics);

    @GET("analytics/{id}")
    Call<Analytics> getAnalytics(@Path("id") int id);

    @GET("lyrics/{id}")
    Call<LyricResponse> getLyrics(@Path("id") int id);

    @POST("songs/{id}/newline")
    Call<GenerateNewLInes> getNewLine(@Path("id") int id);
}
