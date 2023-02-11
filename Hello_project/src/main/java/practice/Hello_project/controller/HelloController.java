package practice.Hello_project.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {

    // getMapping의 헬로는 주소로 받음 http의 겟임
    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!!");

        // return은 templates의 hello.html을 돌려주라는 의미
        return "hello";
    }

    @GetMapping("hello-asdf")
    public String helloMvc(@RequestParam(value = "TEST") String name, Model model) {
        model.addAttribute("TEST", name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("myResponse") String name) {
        return "hello" + name;
    }

    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloAPI(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setnAme(name);
        hello.setNumber(234);
        return hello;
    }

    static class Hello {
        private String nAme;

        public int getNumber() {
            return number;
        }

        public void setNumber(int number) {
            this.number = number;
        }

        private int number;

        public String getnAme() {
            return nAme;
        }

        public void setnAme(String nAme) {
            this.nAme = nAme;
        }
    }
}
