# Python实现汉诺塔问题-测试部分

## 代码

```py
import unittest
from hanoi import move

class HanoiTestCase(unittest.TestCase):
    def test_hanoi(self):
        self.assertEqual(move(1, 'A', 'B', 'C'), 1)
        self.assertEqual(move(2, 'A', 'B', 'C'), 3)
        self.assertEqual(move(3, 'A', 'B', 'C'), 7)

if __name__ == '__main__':
    unittest.main()
```

## 启动命令

```py
pytest test.py --capture=no
```

## 测试样例

![image-20231126153239765](C:\Users\86133\AppData\Roaming\Typora\typora-user-images\image-20231126153239765.png)