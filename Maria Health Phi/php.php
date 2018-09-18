<?php
$x = 11;
$first = 1;
$second = 0;
if($x % 3 && $x % 5) {
  for ($i = 1; $i <= $x; $i++) {
    $nxt = $first + $second;
    $first = $second;
    $second = $nxt;
    echo $nxt . "\n";
  }
} else if($x % 3 == 0 && $x % 5 == 0) {
  echo "Maria Health";
} else {
  if($x % 3 == 0) {
    echo "Maria";
  }
  if($x % 5 == 0) {
    echo "Health";
  }
}
