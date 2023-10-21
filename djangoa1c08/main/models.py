#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class xiangmufenlei(BaseModel):
    __doc__ = u'''xiangmufenlei'''
    __tablename__ = 'xiangmufenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmufenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目分类' )
    '''
    xiangmufenlei=VARCHAR
    '''
    class Meta:
        db_table = 'xiangmufenlei'
        verbose_name = verbose_name_plural = '项目分类'
class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xueshengzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xueshengzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xueshengzhanghao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='学生账号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    mima=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    xueyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学院' )
    zhaopian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='照片' )
    '''
    xueshengzhanghao=VARCHAR
    xueshengxingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    lianxidianhua=VARCHAR
    zhuanye=VARCHAR
    xueyuan=VARCHAR
    zhaopian=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class jiaoshi(BaseModel):
    __doc__ = u'''jiaoshi'''
    __tablename__ = 'jiaoshi'

    __loginUser__='jiaoshigonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='jiaoshigonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoshigonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='教师工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    jiaoshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    zhicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    jiaoshigonghao=VARCHAR
    mima=VARCHAR
    jiaoshixingming=VARCHAR
    xingbie=VARCHAR
    zhicheng=VARCHAR
    lianxidianhua=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshi'
        verbose_name = verbose_name_plural = '教师'
class xueshenghuodongshenbao(BaseModel):
    __doc__ = u'''xueshenghuodongshenbao'''
    __tablename__ = 'xueshenghuodongshenbao'



    __authTables__={'xueshengzhanghao':'xuesheng','jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xueshengzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生账号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    xueyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学院' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    xiangmufenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目分类' )
    shijianxiangmu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='实践项目' )
    xiangmuneirong=models.TextField   (  null=True, unique=False, verbose_name='项目内容' )
    shijianshijian=models.DateField   (  null=True, unique=False, verbose_name='实践时间' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    xueshengzhanghao=VARCHAR
    xueshengxingming=VARCHAR
    xueyuan=VARCHAR
    zhuanye=VARCHAR
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    xiangmufenlei=VARCHAR
    shijianxiangmu=VARCHAR
    xiangmuneirong=Text
    shijianshijian=Date
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'xueshenghuodongshenbao'
        verbose_name = verbose_name_plural = '学生活动申报'
class shehuishijianhuodong(BaseModel):
    __doc__ = u'''shehuishijianhuodong'''
    __tablename__ = 'shehuishijianhuodong'



    __authTables__={'jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shijiantimu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='实践题目' )
    fengmian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='封面' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    xiangguanziliao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='相关资料' )
    xuanbaoyaoqiu=models.TextField   (  null=True, unique=False, verbose_name='选报要求' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    xiangmufenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目分类' )
    baomingrenshu=models.IntegerField  (  null=True, unique=False, verbose_name='报名人数' )
    shijianmude=models.TextField   (  null=True, unique=False, verbose_name='实践目的' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    shijiantimu=VARCHAR
    fengmian=VARCHAR
    jiaoshixingming=VARCHAR
    jiaoshigonghao=VARCHAR
    xiangguanziliao=VARCHAR
    xuanbaoyaoqiu=Text
    shenqingshijian=DateTime
    xiangmufenlei=VARCHAR
    baomingrenshu=Integer
    shijianmude=Text
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'shehuishijianhuodong'
        verbose_name = verbose_name_plural = '社会实践活动'
class huodongbaomingshenqing(BaseModel):
    __doc__ = u'''huodongbaomingshenqing'''
    __tablename__ = 'huodongbaomingshenqing'



    __authTables__={'jiaoshigonghao':'jiaoshi','xueshengzhanghao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shijiantimu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='实践题目' )
    fengmian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='封面' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    xiangmufenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目分类' )
    xueshengzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生账号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    xueyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学院' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    baomingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='报名时间' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    shijiantimu=VARCHAR
    fengmian=VARCHAR
    jiaoshixingming=VARCHAR
    jiaoshigonghao=VARCHAR
    xiangmufenlei=VARCHAR
    xueshengzhanghao=VARCHAR
    xueshengxingming=VARCHAR
    xueyuan=VARCHAR
    zhuanye=VARCHAR
    baomingshijian=DateTime
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'huodongbaomingshenqing'
        verbose_name = verbose_name_plural = '活动报名申请'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '系统公告'
