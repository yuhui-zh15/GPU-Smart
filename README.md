# G-Smart: Interactive Automatic GPU Manager

###### Author: Yuhui Zhang, yuhui-zh15@mails.tsinghua.edu.cn, Tsinghua University

## Version 1.0

### Menu
```
Welcome to Smart GPU Queue
--------------------------
[1] New Command
[2] Running History
[3] Waiting List
[4] GPU Status
--------------------------
```

### New Command
```
Please input command
<Your Command Here>
python idle.py
```

### Running History
```
<Task ID>{GPU ID}{Enqueue Time->Dequeue Time}: Command
[0]{GPU: 0}(Thu Aug 23 08:10:54 2018->Thu Aug 23 08:11:56 2018): python idle.py
[1]{GPU: 1}(Thu Aug 23 08:10:58 2018->Thu Aug 23 08:12:59 2018): python idle.py
[2]{GPU: 2}(Thu Aug 23 08:11:02 2018->Thu Aug 23 08:14:01 2018): python idle.py
[3]{GPU: 3}(Thu Aug 23 08:11:06 2018->Thu Aug 23 08:15:03 2018): python idle.py
```

### Waiting List
```
<Task ID>{Enqueue Time}: Command
[0](Thu Aug 23 08:10:54 2018): python idle.py
[1](Thu Aug 23 08:10:58 2018): python idle.py
[2](Thu Aug 23 08:11:02 2018): python idle.py
[3](Thu Aug 23 08:11:06 2018): python idle.py
```

### GPU Status
```
<Server>  Thu Aug 23 10:27:52 2018
[0] Tesla K20c       | 43'C,   0 % |     0 /  4742 MB |
[1] Tesla K20c       | 44'C,   0 % |     0 /  4742 MB |
[2] Tesla K20c       | 43'C,   0 % |     0 /  4742 MB |
[3] Tesla K20c       | 39'C,  96 % |     0 /  4742 MB |
```
