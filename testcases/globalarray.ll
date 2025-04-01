@x = global [6 x i32] zeroinitializer
define i32 @main() {
.ret:
  %x0 = getelementptr i32, ptr @x, i32 0, i32 0
  call void @println(ptr %x0)
  ret i32 0
}