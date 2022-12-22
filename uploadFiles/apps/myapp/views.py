from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
from myapp.models import SimFiles

# Create your views here.
def index(request):
    return render(request,"myapp/mainPage.html")

#浏览文件
def indexfiles(request):
    try:
        fileslist=SimFiles.objects.all()
        uploadContext={"fileslist":fileslist}
        return render(request, "myapp/download.html", uploadContext)   #加载模板
    except:
        return HttpResponse("没有找到文件信息")

# 加载上传文件
def uploadPage(request):
    return render(request, "myapp/upload.html")

# 上传文件
def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("media", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            # 保存文件名到数据库中
            model = SimFiles(filename=File.name)
            model.save()
            # 指定保存路径
            path = '%s/%s' % (settings.MEDIA_ROOT, File.name)
            print(path)
            # 打开特定的文件进行二进制的写操作;
            with open(path, 'wb+') as f:
                # 分块写入文件;
                for chunk in File.chunks():
                    f.write(chunk)
            return render(request, "myapp/upload.html")
    else:
        return HttpResponse('上传失败')

# 下载文件
from myapp.serializers import FileSerializer
def download_file(request, fileid):
    # 实例化对象
    model = SimFiles.objects.get(id=fileid)
    # 构造序列化对象
    serializer = FileSerializer(model)
    filename = serializer.data['filename']
    filepath = settings.MEDIA_ROOT + '/' + filename # 路径拼接

    file = open(filepath, 'rb')
    response = FileResponse(file, as_attachment=True, filename=filename)
    return response
