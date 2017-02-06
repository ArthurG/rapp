package me.andrewtam.rapp.di;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;
import me.andrewtam.rapp.model.api.RappClient;
import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

@Module
public class ApiModule {

    final String BASE_URL = "http://44186ec2.ngrok.io";

    @Provides
    @Singleton
    public RappClient provideRappClient() {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .client(new OkHttpClient.Builder().build())
                .build();
        return retrofit.create(RappClient.class);
    }
}