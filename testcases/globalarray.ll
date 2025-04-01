@x = global [6 x i64] zeroinitializer
define i64 @main() {
.ret:
  %x0 = getelementptr i64, ptr @x, i64 0, i64 1
  store i64 42, ptr %x0
  %x1 = load i64, ptr %x0
  call void @println(i64 %x1)
  ret i64 0
}