@.str = global [6 x i8] c"hello\00"

define void @printstring(ptr %str) {
.entry:
  call void @printstr(ptr %str)

  ret void
}

define i64 @main() {
.entry:
  
  call void @printstring(ptr @.str)
  
  ret i64 0
}