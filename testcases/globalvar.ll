@x = global i64 -1
define i64 @main() {
.ret:
  %x1 = load i64, ptr @x
  call void @println(i64 %x1)
  ret i64 0
}