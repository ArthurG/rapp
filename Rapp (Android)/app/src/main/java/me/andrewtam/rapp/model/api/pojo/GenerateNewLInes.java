package me.andrewtam.rapp.model.api.pojo;

import com.google.gson.annotations.SerializedName;

/**
 * Created by andrewtam on 2017-02-05.
 */

public class GenerateNewLInes {

    @SerializedName("newlines")
    private String[] newlines;

    public String[] getNewlines() {
        return newlines;
    }

    public void setNewlines(String[] newlines) {
        this.newlines = newlines;
    }
}
