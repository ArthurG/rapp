package me.andrewtam.rapp;

import android.app.Application;

import io.realm.Realm;
import io.realm.RealmConfiguration;
import me.andrewtam.rapp.di.DaggerPresenterComponent;
import me.andrewtam.rapp.di.PresenterComponent;


public class RappApplication extends Application {
    private static PresenterComponent mPresenterComponent;

    @Override
    public void onCreate() {
        super.onCreate();

        initPresenterComponent();

        Realm.init(this);
        RealmConfiguration realmConfig = new RealmConfiguration.Builder().build();
        Realm.deleteRealm(realmConfig); // Delete Realm between app restarts.
        Realm.setDefaultConfiguration(realmConfig);
    }

    public static PresenterComponent getPresenterComponent() {
        return mPresenterComponent;
    }

    private void initPresenterComponent() {
        mPresenterComponent = DaggerPresenterComponent.create();
    }
}
