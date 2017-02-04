package me.andrewtam.rapp.presenter;

import me.andrewtam.rapp.view.View;

interface Presenter<V extends View> {

    void attachView(V view);

    void detachView();
}
