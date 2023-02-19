package Kotlin_study

interface Vehicle {
//    인터페이스에 프로퍼티 선언도 가능하다. 단, 구현 클래스에서 오버라이딩 해줘야함
    val name : String
    fun start()
//    코틀린 인터페이스에서는 기본 구현 메서드 가능
    fun stop() {
        println("Stopped!!")
    }
}
interface Motor {
    fun start()
//    코틀린 인터페이스에서는 기본 구현 메서드 가능
    fun stop() {
        println("Motor stop")
    }
}
class Car(override val name: String = "Genesis") : Vehicle, Motor {
    var speed = 0
    override fun start() {
        speed = 3
        println(speed)
    }

    override fun stop() {
//        코틀린 인터페이스에서 기본 구현메서드도 다중 상속 가능하나 super로 해야함
        super<Vehicle>.stop()
        super<Motor>.stop()
        speed = 0
        println(speed)
    }
}

fun main() {
    val car = Car()
    println(car.name)
    car.start()
    car.stop()

}