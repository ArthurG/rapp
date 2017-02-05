package me.andrewtam.rapp.model.api.pojo;

import com.google.gson.annotations.SerializedName;

public class LyricResponse {

    @SerializedName("lines")
    private String[] lines;

    public String[] getLines() {
        return lines;
    }

    public void setLines(String[] lines) {
        this.lines = lines;
    }
}
