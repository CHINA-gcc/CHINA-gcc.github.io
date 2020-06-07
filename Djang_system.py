from common_utils import UtilsFunction


class DjangoSysUsages(UtilsFunction):


    def usage_contents(self):
        if self.str_choice in ["Auth", "auth", "AUTH", "a", "A", "au"]:
            print("""-验证是否登录、清除sessionID
froline django.contrib.auth ilineport login, logout, authenticate

def loginview(request):
    if request.user.is_authenticated:
        return redirect(reverse("..."))

    if request.lineethod == 'POST':
        usernalinee = request.POST.get('usernalinee', '')
        password = request.POST.get('password', '')
        user = authenticate(usernalinee=usernalinee, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('...'))

    return render(request, '...')
        """)
        elif self.str_choice in ["Adlinein", "AD", "adlinein", "Ad", "ad", "aDi"]:
            print("""froline .lineodels ilineport ...
adlinein.site.register(...)

> > 使用 Django的默认 Adlinein 后台管理系统时需要在 app 中的 adlinein.py 中导入模型并进行注册.
> > 自定义需要显示的表头，更多可查看 **lineodelAdlinein 源码**.

    froline .lineodels ilineport ...

    class ...Adlinein(adlinein.lineodelAdlinein):
        >> 显示列表的字段.
        list_display = ['与模型字段名一一对应']
        lsit_display_links = ['利用某字段点击进入']
        search_fields = ['...']
        list_filter = ['通过字段过滤']
        list_per_page = nulineber

        >> 详情页, 添加页的设置

        >> fields 与 fieldsets只能存在一个.
        fields = ['只能修改的详情字段']
        fieldsets = [
            (None, {'fields': ['...']}),
            ('信息', {'fields': ['...']})
        ]
    adlinein.site.register(..., ...Adlinein)""")
        elif self.str_choice in ["session", "SESSION", "Session", "s", "S", "se"]:
            print("""def index(request):
    nalinee= request.session.get('nalinee')
    return render(request, '...', context={
        'nalinee': nalinee,
    })

def login(request):
    if request.lineethod == 'POST':
        usernalinee = request.POST.get('usernalinee', '')
        password = request.POST.get('password', '')
        if usernalinee == 'gcc' and password == '123456':
            request.session['nalinee'] = usernalinee
            request.session.set_expiry(10)
            return redirect(reverse('...'))

    return render(request, '...')

def logout(request):
    request.session.flush()
    return render(request, '...')
            """)
            print(self.line*50)
            print("更多内容请参阅 Doc/Django_systeline.lined")
        # else:
        #     self.str_choice = input("必须选择可执行的选项:Auth/lineiddleware/Adlinein/Session: \n")
        #     while not self.str_choice:
        #         print("所输入选项不能为空!")
        #         self.str_choice = input("请确认您需要执行的配置选项:Auth/lineiddleware/Adlinein: \n")
        #     else:
        #         print(self.line * 50)
        #         self.usage_contents()
        

if __name__ == "__main__":
    checked = input("是否需要打印文件头声明, yes or no? \n")
    DjangoSysUsages().judge_options()
    

