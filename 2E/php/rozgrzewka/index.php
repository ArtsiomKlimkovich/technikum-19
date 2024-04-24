<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    <?php
        // zad 1
        $randArray = array();
        for ($i = 0; $i < 10; $i++){
            array_push($randArray, rand(10, 99));
        }
        for ($i = 0; $i < count($randArray); $i++){
            echo $randArray[$i] . " ";
        }

        $numsStr = @$POST['liczby'];
        $numsArray = array();

        for ($i = 0; $i < strlen($numsStr); $i+= 2){
            array_push($numsArray, $numsStr[$i]);
        }

        foreach ($numsArray as $n){
            echo $n . " ";
        }
        function bubbleSort(array $array): array{
            for ($i = count($array) - 1; $i > 0; $i--) {
                for ($j = 0; $j < $i; $j++) {
                    if ($array[$j] > $array[$j + 1]) { 
                        $temp = $array[$j];
                        $array[$j] = $array[$j+1];
                        $array[$j+1] = $temp;
                    }
                }
            }
            return $array;
        }
    ?>
    <br><br>
    <form action="s2.php" method="POST">
        <input type="text" name="liczby">
        <input type="submit" name="wyslij" value="wyslij">
    </form>
</body>
</html>
