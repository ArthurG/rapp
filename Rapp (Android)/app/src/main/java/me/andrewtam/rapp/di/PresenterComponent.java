package me.andrewtam.rapp.di;

import javax.inject.Singleton;

import dagger.Component;
import me.andrewtam.rapp.presenter.LyricPresenter;
import me.andrewtam.rapp.presenter.MainPresenter;

@Singleton
@Component(modules = {ApiModule.class})
public interface PresenterComponent {

    void inject(MainPresenter presenter);

    void inject(LyricPresenter presenter);
}
