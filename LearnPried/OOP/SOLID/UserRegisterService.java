public class UserRegisterService {

    public void execute(String id, String password) {
        if (!checkUserExist(id) && checkIdAndPwLength(id, password)) {
            save(id, password);
        }
    }

    private Boolean checkUserExist(String id) {
        // 유저가 존재하나 확인
        // 현재는 임의로 존재하지 않는다는 의미의 False
        return false;
    }

    private Boolean checkIdAndPwLength(String id, String password) {
        // id와 pw의 길이 검열
        return true;
    }

    private void save(String id, String password) {
        // 저장
    }
}
