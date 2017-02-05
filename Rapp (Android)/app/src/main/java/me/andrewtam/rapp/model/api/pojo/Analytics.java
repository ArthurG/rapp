package me.andrewtam.rapp.model.api.pojo;


import com.google.gson.annotations.SerializedName;

public class Analytics {

    @SerializedName("sentiment")
    private double sentiment;

    @SerializedName("keywords")
    private String keywords;

    @SerializedName("syllableArray")
    private int[] syllableArray;

    @SerializedName("rhymeWords")
    private String[] rhymeWords;

    public double getSentiment() {
        return sentiment;
    }

    public void setSentiment(double sentiment) {
        this.sentiment = sentiment;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public int[] getSyllableArray() {
        return syllableArray;
    }

    public void setSyllableArray(int[] syllableArray) {
        this.syllableArray = syllableArray;
    }

    public String[] getRhymeWords() {
        return rhymeWords;
    }

    public void setRhymeWords(String[] rhymeWords) {
        this.rhymeWords = rhymeWords;
    }
}
