public class Galaxy implements Phone {

    @Override
    public void call(String name) {
        System.out.println("빅스비 : "+name+"에게 전화를 겁니다");
    }

    @Override
    public void playMusic(String name) {
        System.out.println("빅스비 : "+name+"을 재생합니다");
    }
}
