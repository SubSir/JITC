@.str = global [6 x i8] c"hello\00"

define i64 @main() {
.entry:
  
  call void @printstr(ptr @.str)
  
  ret i64 0
}