package Java_study.자바_보충;

public class Weapons {
    public static void main(String[] args) {
        Sword weapon = new Sword();
        weapon.atk();
    }
}

class Weapon {}
class Sword extends Weapon {
    public void atk() {
        System.out.println("칼 공격");
    }
}