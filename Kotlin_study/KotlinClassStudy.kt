package Kotlin_study

abstract class Human(protected val nation : String) {
    open fun comeFrom() {
        println("I'm from $nation")
    }
}

//자식의 생성자를 받아 부모의 primary 생성자로 넘겨 줄 수 있다.
class Personal(private val name : String, private val age : Int, nation : String) : Human(nation) {
    private var hobby: String? = null

    //    생성자 오버라이딩 가능 매개변수 갯수가 primary보다 적으면 나머지는 직접 정하는 것도 가능
    constructor(name: String, age: Int) : this(name, age, "Korea")

//    생성자 매개변수 갯수가 primary보다 많으면 그대로 따라감
    constructor(name: String, age: Int, nation: String, hobby : String?) : this(name, age, nation) {
        this.hobby = hobby
    }

    fun introduceMyself() {
        println("My name is $name and I'm ${age}years old")
    }

    override fun comeFrom() {
        println("I love $nation")
    }

    fun introduceHobby() {
        hobby?.let { println("My hobby is $it") }
    }
}

//object는 싱글턴 클래스이다
object X {
    var x = 3
}

fun main() {
    val kim = Personal("KimDongHoon", 15, "Korea")
    val nakamura = Personal("Nakamura", 29, "Japan")
    val lee = Personal("LeeDongGi", 38)
    val park = Personal("ParkHongSu", 23, "Korea", "Baseball")
    kim.comeFrom()
    nakamura.comeFrom()
    lee.comeFrom()
    park.comeFrom()

    kim.introduceMyself()
    nakamura.introduceMyself()
    lee.introduceMyself()
    park.introduceMyself()

    park.introduceHobby()

    println(X.x)

}