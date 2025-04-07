define i64 @add(i64 %a, i64 %b) {
.ret:
  %c = add i64 %a, %b 
  ret i64 %c 
}
 
define i64 @main() {
.ret:
  %d = call i64 @add(i64 1, i64 2)
  ret i64 %d 
}