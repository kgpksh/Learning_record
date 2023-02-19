package Kotlin_study

data class KotlinDataClass(val companyName : String, val name : String, var date : String, var seatNumber : Int)
// toString(), hashCode(), equals(), copy() 등 자동 완성
//println()을 하면 객체 주소가 아니라 데이터가 그대로 출력됨
