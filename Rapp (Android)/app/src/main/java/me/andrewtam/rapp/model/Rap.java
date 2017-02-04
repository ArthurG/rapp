package me.andrewtam.rapp.model;

import java.util.Date;

import io.realm.RealmObject;

public class Rap extends RealmObject {

    private String title;
    private Date date;
    private String length;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }
}
