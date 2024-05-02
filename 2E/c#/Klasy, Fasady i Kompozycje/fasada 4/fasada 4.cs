// Fasada 4
class Client2 { }

class HomeTheaterFacade {
    public void watchMovie() { }
    public void endMovie() { }

    Projector projector;
    SoundSystem soundSystem;
    MediaPlayer mediaPlayer;

    public void addProjector() {
        projector = new Projector();
    }
    public void addSoundSystem() {
        soundSystem = new SoundSystem();
    }
    public void setMediaPlayer(MediaPlayer mediaPlayer) {
        this.mediaPlayer = mediaPlayer;
    }
}

class Projector {
    public void on() { }
    public void off() { }
}

class SoundSystem {
    public void on() { }
    public void off() { }
}

class MediaPlayer {
    public void play() { }
    public void stop() { }
}
