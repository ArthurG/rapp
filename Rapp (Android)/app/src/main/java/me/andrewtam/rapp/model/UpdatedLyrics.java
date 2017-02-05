package me.andrewtam.rapp.model;

import java.util.List;

public class UpdatedLyrics {
    List<String> lines;

    public UpdatedLyrics(List<String> lines) {
        this.lines = lines;
    }

    public List<String> getLines() {
        return lines;
    }

    public void setLines(List<String> lines) {
        this.lines = lines;
    }
}
