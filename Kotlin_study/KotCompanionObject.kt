package Kotlin_study

class Book private constructor(val id : Int, val name : String) {
//    자바의 static과 유사, 인터페이스 구현같은거도 가능
    companion object : IdProvider{
        override fun getID(): Int {
            return 234
        }
        var bookName = "Harry porter"
        fun create() = Book(getID(), bookName)
    }

}

interface IdProvider {
    fun getID() : Int
}

fun main() {
//    private constructor때문에 다음과 같은 방식으로 객체 생성 불가능
//    val book = Book(2, "Harry")

//    대신 다음과 같이 함. Companion 생략 가능
    val book = Book.Companion.create()
    val book2 = Book.create()
    println(Book.bookName)
}