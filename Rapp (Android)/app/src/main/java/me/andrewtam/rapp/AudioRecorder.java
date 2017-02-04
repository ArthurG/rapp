package me.andrewtam.rapp;

import android.media.MediaRecorder;
import android.os.Environment;

import java.io.File;
import java.io.IOException;

public class AudioRecorder {

    private MediaRecorder recorder = new MediaRecorder();
    public final String path;

    public AudioRecorder(String path) {
        this.path = sanitizePath(path);
    }

    private String sanitizePath(String path) {
        if (!path.startsWith("/")) path = "/" + path;
        if (!path.contains(".")) path += System.currentTimeMillis() + ".3gp";
        return Environment.getExternalStorageDirectory().getAbsolutePath() + path;
    }

    public void start() throws IOException {
        if (recorder == null) recorder = new MediaRecorder();
        String state = android.os.Environment.getExternalStorageState();
        if (!state.equals(android.os.Environment.MEDIA_MOUNTED))
            throw new IOException("SD Card is not mounted.  It is " + state + ".");

        // make sure the directory we plan to store the recording in exists
        File directory = new File(path).getParentFile();
        if (!directory.exists() && !directory.mkdirs())
            throw new IOException("Path to file could not be created.");

        recorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        recorder.setOutputFormat(MediaRecorder.OutputFormat.AMR_WB);
        recorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_WB);
        recorder.setOutputFile(path);
        recorder.prepare();
        recorder.start();
    }

    public void stop() throws IOException {
        recorder.stop();
        recorder.reset();
        recorder.release();
        recorder = null;
    }
}

