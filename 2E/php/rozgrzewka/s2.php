<?php
    require_once("index.php");

    $randArray = bubbleSort($randArray);
    for ($i = 0; $i < count($randArray); $i++){
        echo $randArray[$i] . " ";
    }
?>
