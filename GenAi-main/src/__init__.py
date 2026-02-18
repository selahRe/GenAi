import sys
import os
from pathlib import Path

# # 1. 打印调试时的关键信息（看控制台输出）
# print("✅ 当前工作目录(cwd)：", os.getcwd())
# print("⚠️ Python搜索路径(sys.path)：", sys.path)

# # 2. 强制添加项目根目录到sys.path（不管配置如何，先让导入生效）
# # 获取项目根目录（src文件夹的父目录）
# project_root = Path(__file__).parent.parent  # 根据你的目录结构调整！
# # 确保路径是字符串且未重复添加
# project_root_str = str(project_root.absolute())
# if project_root_str not in sys.path:
#     sys.path.insert(0, project_root_str)  # 插入到最前面，优先查找

# 3. 再尝试导入
from ToolExecutor import ToolExecutor
print("👌 导入成功！")