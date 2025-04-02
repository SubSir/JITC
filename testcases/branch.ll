define i64 @main() {
.add:
  %a = add i64 1, 1 
  br label %.ret

.ret:  
  ret i64 %a 
}