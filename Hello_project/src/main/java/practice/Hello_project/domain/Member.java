package practice.Hello_project.domain;

import javax.persistence.*;

@Entity
public class Member {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY) //PK자동 생성 전략(정책)
    private Long id;

//    @Column(name = "username") 만약 db의 컬럼명이 username이면 애너테이션으로 알려줄 수 있다
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
