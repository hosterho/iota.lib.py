$set_seed=$args[0]
-join ([char[]](65..90+57..57)*100 | Get-Random -Count 81 -SetSeed $set_seed)