package me.andrewtam.rapp.model.api;

import me.andrewtam.rapp.model.Lyrics;
import okhttp3.MultipartBody;
import retrofit2.Call;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

public interface RappClient {

    @Multipart
    @POST("newsong")
    Call<Lyrics> sendRapAudio(@Part MultipartBody.Part file);
}
