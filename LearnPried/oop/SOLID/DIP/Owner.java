public class Owner {

    private final Phone phone;

    public Owner(Phone phone){
        this.phone = phone;
    }

    public void call(String targetName) {
        phone.call(targetName);
    }

    public void playMusic(String musicName) {
        phone.call(musicName);
    }

}
