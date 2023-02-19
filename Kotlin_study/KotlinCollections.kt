package Kotlin_study

fun main() {
//    초기화 이후 불변
//    Integer[]
    val arr = arrayOf(1,2,3)
//    특정 타입만 다루는 배열 int[]
    val inarr = intArrayOf(2,3,54,6)
//    불변리스트
    val list = listOf(1,2,3)

//    6을 4번 연속 나열
    val sequencialArr = Array(4,{6})

//    추가, 삭제 등 가능
    val mutableList = mutableListOf(1,2,3)
    val ml = ArrayList<Int>()

    println(arr)
    println(list)
    println(mutableList)
    mutableList.add(3)
    println(mutableList)

    val arrList = ArrayList<Int>()
    arrList.add(23)
    arrList.add(524)
    println(arrList)

//    코틀린식 슬라이싱. index 1에서 2까지. 마지막 인덱스까지 포함한다.
    println(mutableList.slice(1..2))


//    불변맵
    val map = mapOf<String, Int>(
            "A" to 12
            , "B" to 14
    )

    val mutableMap = mutableMapOf<String, Int>(
            "A" to 123
            , "B" to 123342
    )

//    맵들은 파이썬처럼 map[] 으로 읽고 쓸 수 있다


//    *는 배열 안쪽의 원소들을 풀어주는 것. 배열 자체를 넣는 것이 아니다.
    val basicSet = mutableSetOf<Int>(*arr)
}