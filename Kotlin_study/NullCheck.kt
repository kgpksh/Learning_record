package Kotlin_study

fun main() {
//    타입 뒤에 ?을 붙여 null값이 들어가는 것을 가능하게 한다
    var variable : Int?
    variable = 3
    println(variable)
    variable = null
    println(variable)

    var result : Int? = 30
//    다음과 같이 하면 오류가 난다 null값인지 확인이 안되서 그렇다.
//    result + 1

//    이렇게 하면 result가 null 이 아니란 것을 보장해준다
    var resultPlusOne = result!! + 1

//    엘비스 오퍼레이터는 null 체크의 또다른 방법이다.

    var nullableString : String? = "sasad"
//    다음과 같이 ?:를 쓰면 null인 경우에 자동으로 대체할 것을 정할 수 있다
    var elvis = (nullableString ?: "nuulll").uppercase()
    println(elvis)
}