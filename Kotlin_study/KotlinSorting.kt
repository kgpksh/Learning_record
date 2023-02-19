package Kotlin_study

import java.util.Arrays


fun main() {
    val names = arrayOf("AAA", "DD", "BB", "CCC", "DDD", "EEEEE")

//    기본정렬
    names.sort()
    println(Arrays.toString(names))

//    커스텀 정렬
    names.sortWith(compareBy {it.length})
}