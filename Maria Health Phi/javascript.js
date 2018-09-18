var x = 11
var first = 1
var second = 0
if(x % 3 && x % 5) {
  for (var i = 1; i <= x; i++) {
    var nxt = first + second
    first = second
    second = nxt
    console.log(nxt)
  }
} else if(x % 3 == 0 && x % 5 == 0) {
  console.log('Maria Health')
} else {
  if(x % 3 == 0) {
    console.log('Maria')
  }
  if(x % 5 == 0) {
    console.log('Health')
  }
}
