@x = global i32 1
define i32 @main() {
.ret:
  call void @println(ptr @x)
  ret i32 0
}