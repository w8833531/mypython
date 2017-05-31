<?php
    function aa($n){
    if ($n == 1)
        return 1;
    return $n * aa($n - 1);
    }
    echo aa(500);
    echo aa(1000);
