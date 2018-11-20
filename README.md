# Y86
ICS2018 project

## 1 Overview

### 1.1 Development Environment

<table>
  <tbody>
    <tr>
      <td><strong>开发语言</strong></td> <td>JavaScript/HTML/CSS/Python</td>
    </tr>
    <tr>
      <td><strong>浏览器环境</strong></td> <td>Chrome/Firefox/Safari</td>
    </tr>
    <tr>
      <td><strong>第三方库</strong></td>   <td>jQuery/Bootstrap</td>
    </tr>
  </tbody>
</table>

### 1.2 File Organization
本次project的后端代码均在backend目录下，说明如下：
<table>
<tr>
<td>
<table>
  <thead>
        <tr>
            <th>文件名</th><th>文件说明</th>
        </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>backend/kernel.py</strong></td> <td>核心代码，模拟CPU过程</td>
    </tr>
    <tr>
      <td><strong>backend/stages/Fetch.py</strong></td> <td>流水线取指阶段</td>
    </tr>
    <tr>
      <td><strong>backend/stages/Decode.py</strong></td> <td>流水线译码阶段</td>
    </tr>
    <tr>
      <td><strong>backend/stages/Execute.py</strong></td> <td>流水线执行阶段</td>
    </tr>
    <tr>
      <td><strong>backend/stages/Memory.py</strong></td> <td>流水线访存阶段</td>
    </tr>
    <tr>
      <td><strong>backend/stages/WriteBack.py</strong></td> <td>流水线写回阶段</td>
    </tr>
  </tbody>
</table>
</td>
<td>
<table>
  <thead>
        <tr>
            <th>文件名</th><th>文件说明</th>
        </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>backend/others/cc_stat.py</strong></td> <td>状态码与条件码类</td>
    </tr>
    <tr>
      <td><strong>backend/others/constant.py</strong></td> <td>常量的定义</td>
    </tr>
    <tr>
      <td><strong>backend/others/decoder.py</strong></td> <td>预处理.yo文件</td>
    </tr>
    <tr>
      <td><strong>backend/others/Init.py</strong></td> <td>处理.yo文件</td>
    </tr>
    <tr>
      <td><strong>backend/others/little_endian.py</strong></td> <td>处理数字的小端法表示</td>
    </tr>
    <tr>
      <td><strong>backend/encoder/encoder.py</strong></td> <td>处理.ys文件</td>
    </tr>
  </tbody>
</table>
</td>
</tr>
<tr>
<td>
<table>
  <thead>
        <tr>
            <th>文件名</th><th>文件说明</th>
        </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>backend/memory_sys/memory.py</strong></td> <td>内存的实现</td>
    </tr>
    <tr>
      <td><strong>backend/memory_sys/register.py</strong></td> <td>系统寄存器的实现</td>
    </tr>
    <tr>
      <td><strong>backend/memory_sys/piperegister.py</strong></td> <td>流水线寄存器的实现</td>
    </tr>
  </tbody>
</table>
</td>
<td>
</td>
</tr>
</table>

## 2 Usage
<p>
  运行本Y86流水线模拟器需要安装python2.7，目前前端仍未完成，若需要调试，在backend目录下，在终端中输入命令python kernel.py即可。
</p>
<p>
  进入界面后，可选择三种模式中任意一种：1.以.yo文件为输入 2.以.ys文件为输入 3.通过终端动态输入

  选择1、2时，请输入合法的文件路径和文件类型！选择1时，文件名请以.yo为结尾，选择2时，文件名请以.ys为结尾，会在同目录下生成一个对应的.yo文件
    
  例：./test/asum.yo或./test/asum.ys
</p>
<p>
  当前支持的调试功能：
  <ul>
    <li>-show       显示当前的指令集，格式同.yo文件</li>
    <li>-step       步进功能，令流水线过程推进一个时钟周期</li>
    <li>-break addr    设置断点，当程序运行到addr时会暂停执行，addr请使用十六进制表示 <br>  例：-break 0xa</li>
    <li>-continue         执行流水线过程，直至遇到异常状态或断点</li>
    <li>-quit       结束调试</li>
    <li>Instruction Code    <br>支持输入合法的汇编代码，将其加在源代码之后。在该指令后，程序会一直读入汇编代码，直至读到空字符串<br>
    例：<br>
    addq %rax, %rax\n<br>
    addq %rbx, %rbx\n<br>
    \n</li>
  </ul>
</p>

## 3 Features
<ul>
  <li>实现Y86指令集的所有指令</li>
  <li>实现流水线的控制逻辑</li>
  <li>实现iaddq操作</li>
  <li>加入了加载转发优化(见4.57)</li>
  <li>实现了Y86汇编器</li>
  <li>支持动态输入代码，动态调试</li>
</ul>

## 4 Test Cases
test目录下存放了sim中自带的样例，并在/test/new目录下构造了一些新的样例
<table>
  <thead>
    <tr>
      <td>测试文件</td><td>描述</td>
    </tr>
  </thead>
  <tr>
    <td>ex32.yo</td><td>测试转发逻辑(见4.32)</td>
  </tr>
  <tr>
    <td>ex33.yo</td><td>测试转发逻辑(见4.33)</td>
  </tr>
  <tr>
    <td>load_forward.yo</td><td>测试加载转发优化(见4.37)</td>
  </tr>
  <tr>
    <td>overflow.yo</td><td>测试数据溢出</td>
  </tr>
  <tr>
    <td>INS1~4.yo</td><td>测试非法指令</td>
  </tr>
</table>

## To Do List
<ul>
  <li>美化前端界面</li>
  <li>完善调试功能，增加步退等功能</li>
  <li>实现反汇编器</li>
  <li>模拟储存器结构</li>
</ul>
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
