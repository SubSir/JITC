@x = global i64 -1
define i64 @func() {
.ret:
  %x1 = load i64, ptr @x
  ret i64 %x1
}
define i64 @main() {
.ret:
  %x2 = call i64 @func()
  call void @println(i64 %x2)
  ret i64 0
}