@x = global [6 x i64] zeroinitializer  
declare void @println(ptr)  
 
define i64 @main() {  
entry:  
  br label %loop.init   
 
loop.init:   
  %counter = phi i64 [ 0, %entry ], [ %next_counter, %loop.body  ]  
  %exit.cond  = icmp eq i64 %counter, 6  
  br i1 %exit.cond,  label %print_loop.init,  label %loop.body   
 
loop.body:   
  %element.ptr  = getelementptr [6 x i64], ptr @x, i64 0, i64 %counter  
  store i64 %counter, ptr %element.ptr   
  %next_counter = add nuw i64 %counter, 1  
  br label %loop.init   
 
print_loop.init:   
  br label %print.loop   
 
print.loop:   
  %print.idx  = phi i64 [ 0, %print_loop.init  ], [ %next.print.idx,  %print.step  ]  
  %current.ptr  = getelementptr [6 x i64], ptr @x, i64 0, i64 %print.idx   
  call void @println(ptr %current.ptr)   
  %next.print.idx  = add nuw i64 %print.idx,  1  
  %print.exit  = icmp eq i64 %next.print.idx,  6  
  br i1 %print.exit,  label %exit, label %print.step   
 
print.step:   
  br label %print.loop   
 
exit:  
  ret i64 0  
}  