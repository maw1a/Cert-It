package com.college.certificategenerator;

import android.os.Bundle;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.ListResult;
import com.google.firebase.storage.StorageReference;

import java.util.ArrayList;
import java.util.HashMap;

public class ChooseTemplates extends AppCompatActivity {

    private HashMap<String, String> details;
    private StorageReference storageReference;
    private ArrayList<StorageReference> templates;
    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.choose_templates);

        details = new HashMap<>();
        details = (HashMap<String, String>) getIntent().getExtras().get("Details");

        templates = new ArrayList<>();

        storageReference = FirebaseStorage.getInstance().getReference();
        StorageReference dummyRef = storageReference.child("starter-templates/");
        dummyRef.listAll().addOnSuccessListener(new OnSuccessListener<ListResult>() {
            @Override
            public void onSuccess(ListResult listResult) {
                templates.addAll(listResult.getPrefixes());

                mRecyclerView = findViewById(R.id.templatesRecyclerView);
                mRecyclerView.setHasFixedSize(true);
                mLayoutManager = new LinearLayoutManager(ChooseTemplates.this);
                mAdapter = new TemplatesAdapter(templates);
                mRecyclerView.setLayoutManager(mLayoutManager);
                mRecyclerView.setAdapter(mAdapter);
            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Toast.makeText(ChooseTemplates.this, e.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}