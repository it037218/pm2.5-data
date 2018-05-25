<?php

   $redis = new Redis();

$redis->connect('127.0.0.1', 6379);
    $keys = $redis->keys("*");
    foreach ($keys as $value){
        echo $value;
        var_dump($redis->get($value));
    }
?>