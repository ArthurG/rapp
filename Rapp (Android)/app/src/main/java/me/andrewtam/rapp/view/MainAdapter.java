package me.andrewtam.rapp.view;

import android.content.Context;
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
import me.andrewtam.rapp.model.Rap;

public class MainAdapter extends RealmRecyclerViewAdapter<Rap, MainAdapter.Holder> implements RecyclerView.OnClickListener{

    public MainAdapter(@NonNull Context context, @Nullable OrderedRealmCollection<Rap> data, boolean autoUpdate) {
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
        Rap obj = getData().get(position);
//        holder.title.setText(obj.getTitle());
//        holder.date.setText(obj.getDate().toString());
//        holder.length.setText(obj.getLength());
    }

    @Override
    public void onClick(View view) {
        int itemPosition =  get getChildLayoutPosition(view);
        String item = mList.get(itemPosition);
        Toast.makeText(mContext, item, Toast.LENGTH_LONG).show();
    }

    class Holder extends RecyclerView.ViewHolder {
        @BindView(R.id.title) TextView title;
        @BindView(R.id.date) TextView date;
        @BindView(R.id.length) TextView length;

        public Holder(View itemView) {
            super(itemView);
            ButterKnife.bind(this, itemView);
        }
    }
}
