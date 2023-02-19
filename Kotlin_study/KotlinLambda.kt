package Kotlin_study

fun main() {
//    기본
//    val basicLambda : (Int, Int) -> Int
    val basicLambda = {a : Int, b : Int -> Int
        a * b}

//    람다에 매개변수가 1개밖에 없으면 it으로 대체 가능
    var nonItLambda = {a : Int ->
        2*a}
    var itLambda : (Int) -> Int = {it * 5}

//    객체 자기자신을 람다식 내부로 옮기는 let 함수
    val testString = "abc"
    println(testString.let { testString.uppercase() })

    val name = "Jack"
    println(name.studentIntro())
    println(extendAnother("Jack", 23))

    val lambda = {number : Double -> number == 4.3213}


    println(invokeLambda(lambda))
    println(invokeLambda({it > 4.3213}))
//    함수의 마지막 파라미터가 람다일때는 소괄호 생략 가능
    println(invokeLambda { it > 3.23 })
//    만약 다른 파라미터가 있다면 이런식으로 - 여기서는 람다 앞에 정수 파라미터 하나 있다 가정
//    invokeLambda(3) {it > 2.32}
}

//확장함수
val studentIntro : String.() -> String = {
//    this는 여기서는 String.()임
    this + " is student"
}

//확장함수의 또다른 예시, 사용법
fun extendAnother(name : String, age : Int) : String{
    val introduceMyself : String.(Int) -> String = {"My name is $this and I'm $it years old"}
    return name.introduceMyself(age)
}

//람다의 또다른 방법
fun invokeLambda(lambda : (Double) -> Boolean) : Boolean {
    return lambda(5.2343)
}
