@x = global [6 x i64] zeroinitializer  
declare void @println(i64)  
 
define i64 @main() {  
.entry:  
  br label %.loopinit   
 
.loopinit:   
  %counter = phi i64 [ 0, %.entry ], [ %next_counter, %.loopbody  ]  
  %exitcond  = icmp eq i64 %counter, 6  
  br i1 %exitcond,  label %.print_loopinit,  label %.loopbody   
 
.loopbody:   
  %elementptr  = getelementptr ptr, ptr @x, i64 0, i64 %counter  
  store i64 %counter, ptr %elementptr   
  %next_counter = add i64 %counter, 1  
  br label %.loopinit   
 
.print_loopinit:   
  br label %.printloop   
 
.printloop:   
  %printidx  = phi i64 [ 0, %.print_loopinit  ], [ %nextprintidx,  %.printstep  ]  
  %currentptr  = getelementptr ptr, ptr @x, i64 0, i64 %printidx   
  %current  = load i64, ptr %currentptr
  call void @println(i64 %current)   
  %nextprintidx  = add i64 %printidx,  1  
  %printexit  = icmp eq i64 %nextprintidx,  6  
  br i1 %printexit,  label %.exit, label %.printstep   
 
.printstep:   
  br label %.printloop   
 
.exit:  
  ret i64 0  
}  