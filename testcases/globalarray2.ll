@x = global [6 x i64] zeroinitializer
define void @func() {
.ret:
  %x0 = getelementptr i64, ptr @x, i64 0, i64 1
  store i64 42, ptr %x0
  ret void
}
define i64 @main() {
.ret:
  call void @func()
  %x1 = getelementptr i64, ptr @x, i64 0, i64 1
  %x2 = load i64, ptr %x1
  call void @println(i64 %x2)
  ret i64 0
}