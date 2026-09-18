package com.gsterling.press;

import android.app.WallpaperManager;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.Rect;
import android.util.DisplayMetrics;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import android.app.Activity;

public class MainActivity extends Activity {
  TextView status, detail; Button protectedStep, finish;
  @Override protected void onCreate(Bundle state) {
    super.onCreate(state); setContentView(R.layout.activity_main);
    status=findViewById(R.id.status); detail=findViewById(R.id.detail);
    protectedStep=findViewById(R.id.continueProtected); finish=findViewById(R.id.finish);
    findViewById(R.id.installTheme).setOnClickListener(v -> install());
    protectedStep.setOnClickListener(v -> openSamsung()); finish.setOnClickListener(v -> home());
  }
  private void install() {
    try {
      status.setText("INSTALLING ABYSS…"); detail.setText("Applying approved Home + Lock masters.");
      WallpaperManager wm=WallpaperManager.getInstance(this);
      apply(wm,R.drawable.abyss_001_home_clockfree,WallpaperManager.FLAG_SYSTEM);
      apply(wm,R.drawable.abyss_001_lock_clockfree,WallpaperManager.FLAG_LOCK);
      getPreferences(MODE_PRIVATE).edit().putBoolean("abyss_wallpapers",true).apply();
      status.setText("ABYSS CORE INSTALLED ✓");
      detail.setText("Artwork is installed. Samsung requires confirmation for protected icon/lock-screen operations.");
      protectedStep.setVisibility(View.VISIBLE); finish.setVisibility(View.VISIBLE);
    } catch(Exception e) {
      status.setText("INSTALLATION NEEDS ATTENTION");
      detail.setText(e.getMessage()==null?"ABYSS could not be fully applied.":e.getMessage());
    }
  }
  private void apply(WallpaperManager wm,int id,int flag) throws Exception {
    Bitmap source=BitmapFactory.decodeResource(getResources(),id);
    if(source==null) throw new IllegalStateException("Approved ABYSS artwork is missing.");
    DisplayMetrics dm=getResources().getDisplayMetrics();
    int targetW=dm.widthPixels, targetH=dm.heightPixels;
    float scale=Math.max((float)targetW/source.getWidth(),(float)targetH/source.getHeight());
    int scaledW=Math.round(source.getWidth()*scale), scaledH=Math.round(source.getHeight()*scale);
    Bitmap scaled=Bitmap.createScaledBitmap(source,scaledW,scaledH,true);
    int left=Math.max(0,(scaledW-targetW)/2), top=Math.max(0,(scaledH-targetH)/2);
    Bitmap phone=Bitmap.createBitmap(scaled,left,top,Math.min(targetW,scaledW-left),Math.min(targetH,scaledH-top));
    wm.suggestDesiredDimensions(targetW,targetH);
    wm.setBitmap(phone,null,false,flag);
    if(phone!=scaled) phone.recycle();
    if(scaled!=source) scaled.recycle();
    source.recycle();
  }
  private void openSamsung() {
    String[] pkgs={"com.samsung.android.themedesigner","com.samsung.android.goodlock"};
    for(String p:pkgs){ Intent i=getPackageManager().getLaunchIntentForPackage(p); if(i!=null){startActivity(i);return;} }
    Toast.makeText(this,"Samsung Theme Park/Good Lock is needed for the protected finishing step.",Toast.LENGTH_LONG).show();
  }
  private void home(){Intent i=new Intent(Intent.ACTION_MAIN);i.addCategory(Intent.CATEGORY_HOME);i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);startActivity(i);}
}