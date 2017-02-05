package me.andrewtam.rapp.model.api;

import java.util.ArrayList;

import me.andrewtam.rapp.model.Lyrics;
import me.andrewtam.rapp.model.UpdatedLyrics;
import okhttp3.MultipartBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Path;

public interface RappClient {

    @Multipart
    @POST("newsong")
    Call<Lyrics> sendRapAudio(@Part MultipartBody.Part file);

    @POST("songs/{id}")
    Call<Lyrics> sendUpdate(@Path("id") int id, @Body UpdatedLyrics updated_Lyrics);
}
