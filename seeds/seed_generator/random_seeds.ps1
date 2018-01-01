for($y=0; $y -le 25;$y++){
  for($i=-1000; $i -le 1000;$i++){
  $random_number = (Get-Random -Maximum 2147483647)
    -join ([char[]](65..90+57..57)*100 | Get-Random -Count 81 -SetSeed (($random_number)+$i))
  }
}
