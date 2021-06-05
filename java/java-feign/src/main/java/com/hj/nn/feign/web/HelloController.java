package com.hj.nn.feign.web;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

/**
 * @Author: hejian
 * @DateTime: 2021/5/27 18:30
 * @Description:
 */
@RestController
@RequestMapping("/feign")
public class HelloController {

    @Autowired
    private NodeClient nodeClient;

    @GetMapping("/hello")
    public Mono<String> hello() {
        return Mono.just(nodeClient.hello());
    }

}
