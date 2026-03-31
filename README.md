# Vein Dataset Management

A small Django-based web UI for managing venous disease patient data. The project provides a front-end built with the Argon theme and placeholder pages for patient list, patient creation, settings and about pages. It uses SQLite by default for quick local development.

Key points
- Django project: `vein_dataset_management`
- Main app: `portal` (UI placeholders and routes)
- Templates and static assets included under `templates/` and `static/` (Argon theme)
- Default DB: `db.sqlite3` (see `vein_dataset_management/settings.py`)

Quick start (Windows / PowerShell)
1. Create and activate a virtual environment in the project root:
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate.ps1`
2. Install Django (tested with Django 5.2.x):
   - `python -m pip install Django`  # or install from `requirements.txt` if you add one
3. Run migrations (if you add models later):
   - `python manage.py migrate`
4. Run the development server on port 8001:
   - `python manage.py runserver 8001`
   - Visit `http://127.0.0.1:8001/`

Notes
- `.venv` is ignored via `.gitignore`; do not commit the virtual environment.
- This repository currently contains UI placeholders. Connect to a real backend or add models/views to persist patient data.

Contributing
- Open an issue or submit a pull request.

License
- Add a license file if you intend to publish this project publicly.

---

# 静脉数据管理

这是一个用于管理静脉疾病患者数据的 Django 项目，包含基于 Argon 主题的前端界面模板。目前主要为界面占位页：患者列表、新建患者、设置与关于页面。默认开发环境使用 SQLite 数据库，便于本地快速启动。

主要信息
- Django 项目：`vein_dataset_management`
- 主应用：`portal`（包含路由与界面模板占位）
- 模板与静态资源位于 `templates/` 和 `static/`（使用 Argon 主题）
- 默认数据库：`db.sqlite3`（查看 `vein_dataset_management/settings.py`）

快速开始（Windows / PowerShell）
1. 在项目根目录创建并激活虚拟环境：
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate.ps1`
2. 安装 Django（已在本仓库中使用 Django 5.2.x 测试）：
   - `python -m pip install Django`
3. 运行迁移（如添加模型后需要执行）：
   - `python manage.py migrate`
4. 在 8001 端口启动开发服务器：
   - `python manage.py runserver 8001`
   - 打开 `http://127.0.0.1:8001/`

说明
- `.venv` 已在 `.gitignore` 中忽略，请不要将虚拟环境提交到仓库。
- 当前仓库主要为 UI 占位，需添加后端逻辑或模型以实现数据持久化。

贡献
- 欢迎开 issue 或提交 PR。

许可
- 若准备公开发布，请补充许可证文件（LICENSE）。
