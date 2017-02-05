package me.andrewtam.rapp.model;


import com.google.gson.annotations.SerializedName;

public class Lyrics {
    @SerializedName("id")
    public int id;

    @SerializedName("lines")
    public String[] lines;


    //To update a song
//    post to /songs/song_id the following
//    {
//        'lines': ['a bunch of transcribed lines', 'afsdfsadg', 'afdsf', 'etc']
//    }
//    //You'll get back the following
//    {
//        'lines': ['a bunch of transcribed lines', 'afsdfsadg', 'afdsf', 'etc']
//    }

}
