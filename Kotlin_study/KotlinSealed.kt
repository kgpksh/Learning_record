package Kotlin_study

// Enum하고 다르게 유연한 클래스.
// sealed는 추상클래스이다. sealed의 서브 클래스들은 반드시 같은 파일 내에 선언되어야 한다. 그렇기에 자신을 상속 받는 서브클래스의 종류를 제한 가능
// 단, sealed 클래스의 서브 클래스를 상속한 클래스들은 같은 파일 내에 없어도 됨
// 서브 클래스들은 class, data, object 모두 가능하다
// sealed는 private 생성자만 가진다.

sealed class Color {
    data class Red(val r : Int, val g : Int, val b : Int) : Color()
    data class Yellow(val r : Int, val g : Int, val b : Int) : Color()
}

fun main() {
    val red = Color.Red(255, 0, 0)
    val coolRed = Color.Red(255, 0, 20)
    val yellow = Color.Yellow(255, 255, 0)
    val coolYellow = Color.Yellow(255, 255, 20)
    println(red)
    colorTeller(red)
    colorTeller(coolRed)

    println(isCoolRed(red))
    println(isCoolRed(coolRed))
}

fun colorTeller(color : Color) {
    when(color) {
        is Color.Red -> println("빨강")
        is Color.Yellow -> println("노랑")
    }
}

fun isCoolRed(color: Color.Red) : Boolean {
    if (color.b >= 20) {
        return true
    }

    return false
}