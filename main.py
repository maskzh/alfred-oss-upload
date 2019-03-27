query = "{query}"
import time
import oss2
import json

from AppKit import NSPasteboard, NSPasteboardTypePNG, NSFilenamesPboardType

endpoint = 'oss-cn-hangzhou.aliyuncs.com'
bucket_name = 'maskzh'
access_key_id = 'xxxxxx'
access_key_secret = 'xxxxxx'

cdn = 'https://static.example.com'
prefix = 'assets/'

exts = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg', 'webp']

def get_paste_file():
  """
  将剪切板数据保存到本地文件并返回文件路径
  """
  pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
  data_type = pb.types()  # 获取剪切板数据的格式类型

  # 根据剪切板数据类型进行处理
  if NSPasteboardTypePNG in data_type:          # PNG处理
    data = pb.dataForType_(NSPasteboardTypePNG)
    filename = '%s.png' % int(time.time())
    filepath = '/tmp/%s' % filename            # 保存文件的路径
    ret = data.writeToFile_atomically_(filepath, False)    # 将剪切板数据保存为文件
    if ret:   # 判断文件写入是否成功
      return filepath

  elif NSFilenamesPboardType in data_type:
    # file in machine
    return pb.propertyListForType_(NSFilenamesPboardType)[0]

def upload_file():
  file_uri = get_paste_file()
  if not file_uri:
    return

  auth = oss2.Auth(access_key_id, access_key_secret)
  bucket = oss2.Bucket(auth, 'http://' + endpoint, bucket_name)
  
  # 生成文件名，格式为 YYYY-MM-DD-FILENAME.EXT
  file_name = file_uri[file_uri.rfind('/') + 1:]
  file_ext = file_name[file_name.rfind('.') + 1:].lower()
  date = time.strftime("%Y-%m-%d-", time.localtime())
  key = prefix + date + file_name

  # 将地址域名改为 CDN 域名，并加上图片处理后缀
  result = bucket.put_object_from_file(key, file_uri)
  url = result.resp.response.url.replace('%2F', '/', 3)
  url = url.replace('http://' + bucket_name + '.' + endpoint, cdn)
  if file_ext in exts:
    url = url + '!default'

  print(url)

if __name__ == '__main__':
  upload_file()
