# OSSUpload

OSS 结合 Alfred WorkFlow 来上传文件

- 使用 python 语言
- 使用 pipenv 来管理 python 版本和包依赖
- 依赖两个包 oss2 和 pyobjc

PS：**pipenv 不是必须的**

## 初始化

```bash
pipenv install
```

pipenv 的 lock 比较慢，可以使用`--skip-lock`跳过。

## 配置

修改 [main.py](./main.py)

|    配置项   | 描述 | 值 |
| ---------- | --- | --- |
| endpoint | 访问域名 | oss-cn-hangzhou.aliyuncs.com |
| bucket_name | 存储空间名称 | - |
| access_key_id | Access Key ID | - |
| access_key_secret | Access Key Secret | - |
| cdn | CDN 域名 | https://static.example.com |
| prefix | 上传目录 | assets/ |

## 运行

复制一张图片，然后

```bash
pipenv run python main.py
```

## Alfred 中的设置

```bash
cd _target_dir_
/usr/local/bin/pipenv run python main.py
```

更多见 [OSSUpload.alfredworkflow](./OSSUpload.alfredworkflow)