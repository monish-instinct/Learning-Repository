$characters = '0123456789abcdefghijklmnopqrstuvwxyz';
$charactersLength = strlen($characters);
$coder = '';
for ($i = 0; $i < 6; $i++)
  $coder .= $characters[rand(0, $charactersLength - 1)];
