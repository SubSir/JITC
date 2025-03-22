define i32 @add(i32 %a, i32 %b) {
.ret:
  %c = add i32 %a, %b 
  ret i32 %c 
}
 
define i32 @main() {
.ret:
  %a = call i32 @add(i32 1, i32 2)
  ret i32 %a 
}