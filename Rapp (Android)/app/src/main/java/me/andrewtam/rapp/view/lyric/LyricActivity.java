package me.andrewtam.rapp.view.lyric;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;
import io.realm.Realm;
import me.andrewtam.rapp.R;
import me.andrewtam.rapp.presenter.LyricPresenter;
import me.andrewtam.rapp.view.View;

public class LyricActivity extends AppCompatActivity implements LyricView {

    private Realm realm;
    private LyricPresenter presenter;

    @BindView(R.id.lyrikz)
    TextView tv;

    @BindView(R.id.sentiment) TextView sentiment;
    @BindView(R.id.keywords) TextView keywords;
    @BindView(R.id.syllable) TextView syllable;
    @BindView(R.id.rhyme) TextView rhyme;
    @BindView(R.id.button2) TextView genButton;

    private int pk;
    @Override
    protected void onStart() {
        super.onStart();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        //realm.close();
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lyric);

        Bundle bundle = getIntent().getExtras();
        pk = bundle.getInt("id");

        ButterKnife.bind(this);
        presenter = new LyricPresenter(pk);
        presenter.attachView(this);

        presenter.loadAnalytics();
        presenter.loadLyrics();
//        Bundle bundle = getIntent().getExtras();
//        pk = bundle.getInt("id");
//        Log.d("FUCK", "pk is " + pk);
//        realm = Realm.getDefaultInstance();
//        Lyrics dur = realm.where(Lyrics.class).equalTo("id", pk).findFirst();
//        for(Tag tag : dur.getLines()) {
//            tv.append(tag.getValue());
//        }
    }

    @Override
    public void setView(String[] lines) {
        if(lines.length == 0) tv.append("WTF???");
        for(String line : lines) tv.append(line);
    }


    @Override
    public void setSentiment(double s) {
        sentiment.setText("Sentiment: " + s);
    }

    @Override
    public void setKeywords(String s) {
        keywords.setText("Tags: " + s);
    }

    @Override
    public void setSyllable(int[] s) {
        syllable.append("Syllables: ");
        for(int i : s) syllable.append(i + " ");
    }

    @Override
    public void setRhyme(String[] r) {
        rhyme.append("Rhymes: ");
        for(String s : r) rhyme.append(s + ", ");
    }

    @OnClick(R.id.button2)
    public void generate(android.view.View v) {
        presenter.newLine();
    }


    @Override
    public void getNextLyric(String[] s) {
        tv.append("-----\n");
        for(String line : s) tv.append(line + "\n");
    } // GIVE UP NOW

}
