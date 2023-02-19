package Kotlin_study

fun main() {
//    메서드 레퍼런스를 ::를 이용해 쓸 수 있다.
    val f = ::add
    println(f(2,5))

}

fun add(x : Int, y : Int) : Int{
    return x + y
}

