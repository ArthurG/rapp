package me.andrewtam.rapp.view.lyric;


import me.andrewtam.rapp.view.View;

public interface LyricView extends View {
    void setView(String[] lines);

    void setSentiment(double s);

    void setKeywords(String s);

    void setSyllable(int[] s);

    void setRhyme(String[] r);

    void getNextLyric(String[] s);
}
