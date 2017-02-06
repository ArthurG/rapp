package me.andrewtam.rapp.view.main;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v7.widget.RecyclerView;
import android.view.*;
import android.view.View;
import android.widget.TextView;

import butterknife.BindView;
import butterknife.ButterKnife;
import io.realm.OrderedRealmCollection;
import io.realm.RealmRecyclerViewAdapter;
import me.andrewtam.rapp.R;
import me.andrewtam.rapp.model.api.pojo.Lyrics;
import me.andrewtam.rapp.view.lyric.LyricActivity;

public class MainAdapter extends RealmRecyclerViewAdapter<Lyrics, MainAdapter.Holder> {

    public MainAdapter(@NonNull Context context, @Nullable OrderedRealmCollection<Lyrics> data, boolean autoUpdate) {
        super(context, data, autoUpdate);
    }

    @Override
    public Holder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_rap, parent, false);
        //itemView.setOnClickListener(this);
        return new Holder(itemView);
    }

    @Override
    public void onBindViewHolder(Holder holder, int position) {
        Lyrics obj = getData().get(position);
        holder.title.setText(obj.getTitle());
        holder.date.setText(obj.getDate());
        holder.length.setText(obj.getLength());
    }


    class Holder extends RecyclerView.ViewHolder implements View.OnClickListener{
        @BindView(R.id.title) TextView title;
        @BindView(R.id.date) TextView date;
        @BindView(R.id.length) TextView length;

        @Override
        public void onClick(View view) {
            Lyrics obj = getData().get(getAdapterPosition());
            Intent myIntent = new Intent(context, LyricActivity.class);
            myIntent.putExtra("id", obj.getId());
            context.startActivity(myIntent);
        }

        public Holder(View itemView) {
            super(itemView);
            ButterKnife.bind(this, itemView);
            itemView.setOnClickListener(this);
        }
    }
}
