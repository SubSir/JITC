# JITC
一个简单的LLVM JIT编译器

## **简化的 LLVM 语法**

### **模块结构**
- 一个模块由多个顶层定义组成：
  - 函数定义
  - 函数声明
  - 全局变量声明
  - 字符串声明
  - 自定义类型

```llvm
module:
  [ function | function_declare | globalvariable | string_declare | typedelcare ]*
```

---

### **类型**
支持以下基本类型：
- `i32`：32位整数
- [TODO] `ptr`：指针类型
- `void`：空类型（用于无返回值函数）
- `i1`：布尔类型（1位整数）

```llvm
type:
  i32 | ptr | void | i1
```

---

### **标识和常量**
- **整数常量**：`-?[0-9]+`
- **标签**：以 `.` 开头，后接字母、数字或下划线（如 `.label1`）。
- **私有变量**：以 `%` 开头（如 `%var`）。
- **全局变量**：以 `@` 开头（如 `@global_var`）。
- **字符串字面量**：用双引号括起来（如 `"hello world"`）。

```llvm
INTEGER:
  -?[0-9]+

Label:
  '.' [a-zA-Z_] [a-zA-Z0-9_]*

Privatevariable:
  '%' Identifier

Global_var:
  '@' (~[@ \r\n(),])+  // 非 @、换行或逗号的字符

StringLiteral:
  '"' (~["])+ '"'
```

---

### **函数声明**
- 声明一个函数，但不定义其具体实现。
- 格式：`declare` 返回类型 函数名 `(参数类型列表)`

```llvm
function_declare:
  declare type Global_var '(' types? ')'
```

**示例**：
```llvm
declare i32 @my_function(i32, i1)
declare void @print()
```

---

### **函数定义**
- 定义一个函数的具体实现。
- 格式：`define` 返回类型 函数名 `(参数列表)` `{ 基本块 }`

```llvm
function:
  define type Global_var '(' params? ')' '{' basic_block+ '}'
```

**示例**：
```llvm
define i32 @add(i32 %a, i32 %b) {
.entry:
  %sum = add i32 %a, %b
  ret i32 %sum
}
```

---

### **自定义类型**
- 定义复合类型（例如结构体）。
- 格式：`%name = type { 类型列表 }`

```llvm
typedelcare:
  Privatevariable '=' 'type' '{' types? '}'
```

**示例**：
```llvm
%my_struct = type { i32, i32 }
```

---

### **全局变量声明**
- 声明全局变量或字符串。
- 格式：
  - 普通变量：`@name = global 类型 常量`
  - 字符串变量：`@name = global [N x i8] c"字符串"`
  - 静态数组：`@name = global [N x 类型] zeroinitializer`

```llvm
globalvariable:
  Global_var '=' 'global' type (constant|string_constant)

string_declare:
  Global_var '=' 'global' '[' INTEGER 'x' 'i8' ']' 'c' StringLiteral

globalarray:
  Global_var '=' 'global' '[' INTEGER 'x' type ']' 'zeroinitializer'
```

**示例**：
```llvm
@global_int = global i32 42
@my_string = global [13 x i8] c"Hello, world"
```

---

### **指令**
指令包括以下类型：

1. **返回指令**
   ```llvm
   ret type value?
   ```

   **示例**：
   ```llvm
   ret i32 0
   ret void
   ```

2. **调用指令**
   ```llvm
   call type Global_var '(' params? ')'
   Privatevariable '=' call type Global_var '(' params? ')'
   ```

   **示例**：
   ```llvm
   call void @print()
   %result = call i32 @add(i32 %a, i32 %b)
   ```

   此外，还支持内建函数：
   ```llvm
   call void @print(i32 %val)
   call void @println(i32 %val)
   call void @printstr(ptr %str)
   call i32 @input()
   ```

3. **二元操作**
   ```llvm
   Privatevariable '=' bin_op type value ',' value
   ```

   - 支持操作符：`add`、`sub`、`mul`、`sdiv`、`srem`、`shl`、`ashr`、`and`、`or`、`xor`

   **示例**：
   ```llvm
   %sum = add i32 %a, %b
   ```

4. **跳转指令**
   ```llvm
   br label %Label
   br i1 value, label %Label1, label %Label2
   ```

   **示例**：
   ```llvm
   br label %end
   br i1 %cond, label %true_block, label %false_block
   ```

5. **加载和存储指令**
   - 加载：从内存中读取值
     ```llvm
     Privatevariable '=' load type, ptr var
     ```
   - 存储：将值写入内存
     ```llvm
     store type value, ptr var
     ```

   **示例**：
   ```llvm
   %val = load i32, ptr %ptr
   store i32 %val, ptr %ptr
   ```

6. **取指针指令**
   ```llvm
   Privatevariable '=' getelementptr ptrtype, ptr var, i32 value
   Privatevariable '=' getelementptr ptrtype, ptr var, i32 INTEGER, i32 value
   ```

   **示例**：
   ```llvm
   %ptr = getelementptr i32, ptr %array, i32 0, i32 %index
   ```

7. **比较指令**
   ```llvm
   Privatevariable '=' icmp cond type value ',' value
   ```

   - 条件：`eq`、`ne`、`slt`、`sgt`、`sle`、`sge`

   **示例**：
   ```llvm
   %cmp = icmp eq i32 %a, %b
   ```

8. **Phi 指令**
   ```llvm
   Privatevariable '=' phi type [ value, %Label ](, [ value, %Label ])+
   ```

   **示例**：
   ```llvm
   %result = phi i32 [ 0, %entry ], [ %sum, %loop ]
   ```

---

### **基本块**
- 格式：`Label: 指令列表`
- 一个函数由多个基本块组成。

```llvm
basic_block:
  Label':' instruction+
```

**示例**：
```llvm
.entry:
  %sum = add i32 %a, %b
  br label %exit

.exit:
  ret i32 %sum
```

---

### **参数和类型列表**
- 参数列表定义函数参数。
- 类型列表用于复合类型声明。

```llvm
params:
  [ parameter (',' parameter)* ]

parameter:
  type Privatevariable | type Global_var | type constant

types:
  [ type (',' type)* ]
```

**示例**：
```llvm
i32 %a, i32 %b
i32, i1
```

---

### **值和常量**
- 值可以是变量或常量。
- 常量包括整数或 `null`。
- 变量可以是私有变量或全局变量。

```llvm
value:
  Privatevariable | constant | Global_var

constant:
  INTEGER | 'null'
```

**示例**：
```llvm
42
null
%var
@global_var
```

---