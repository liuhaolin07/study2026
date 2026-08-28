# 自动化测试

运行：

```powershell
.\tests\run_tests.ps1
```

`header_probe.cpp` 逐个验证头文件自包含，`test_templates.cpp` 验证算法结果和边界条件，`odr_probe.cpp` 验证头文件可被多个翻译单元同时包含。编译参数包含 `-Wall -Wextra -Werror`，警告也会导致测试失败。
