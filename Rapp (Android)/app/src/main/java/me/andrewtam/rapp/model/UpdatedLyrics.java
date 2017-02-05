package me.andrewtam.rapp.model;

import java.util.List;

/**
 * Created by andrewtam on 2017-02-04.
 */

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
