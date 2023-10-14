<?php

$command = escapeshellcmd('python C:\xampp\htdocs\fajrin\tablecuan.com\main.py');
$run = shell_exec($command);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div class="ortu">

    </div>

</body>

</html>


<script>
    const data = <?php echo $run; ?>;
    const field = document.querySelector("div.ortu");

    for (i = 0; i < Object.keys(data).length; i++) {
        var d = data.data_+{i};
        var x = '<div class="child"> '+d+' </div>'
        field.innerHTML += x;
    }
</script>