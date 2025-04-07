define i64 @add(i64 %a, i64 %b) {
.ret:
  %c = add i64 %a, %b 
  ret i64 %c 
}

define i64 @ad(i64 %d, i64 %e) {
.ret:
  %f = call i64 @add(i64 %d, i64 %e)
  ret i64 %f
}
 
define i64 @main() {
.ret:
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  %h = call i64 @ad(i64 1, i64 2)
  ret i64 %h 
}