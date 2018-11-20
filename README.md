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
