define i64 @add(i64 %a, i64 %b) {
.ret:
  %c = add i64 %a, %b 
  ret i64 %c 
}

define i64 @ad(i64 %a, i64 %b) {
.ret:
  %c = call i64 @add(i64 %a, i64 %b)
  ret i64 %c
}
 
define i64 @main() {
.ret:
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  call i64 @ad(i64 1, i64 2)
  %a = call i64 @ad(i64 1, i64 2)
  ret i64 %a 
}