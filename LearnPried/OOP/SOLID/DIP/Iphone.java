public class Iphone implements Phone {

    @Override
    public void call(String name) {
        System.out.println("시리 : "+name+"에게 전화를 겁니다");
    }

    @Override
    public void playMusic(String name) {
        System.out.println("시리 : "+name+"노래를 틉니다");
    }
}
