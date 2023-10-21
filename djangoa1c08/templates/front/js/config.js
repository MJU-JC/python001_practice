
var projectName = '大学生社会实践申报系统的设计与实现';
/**
 * 轮播图配置
 */
var swiper = {
	// 设定轮播容器宽度，支持像素和百分比
	width: '100%',
	height: '400px',
	// hover（悬停显示）
	// always（始终显示）
	// none（始终不显示）
	arrow: 'none',
	// default（左右切换）
	// updown（上下切换）
	// fade（渐隐渐显切换）
	anim: 'default',
	// 自动切换的时间间隔
	// 默认3000
	interval: 2000,
	// 指示器位置
	// inside（容器内部）
	// outside（容器外部）
	// none（不显示）
	indicator: 'outside'
}

/**
 * 个人中心菜单
 */
var centerMenu = [{
	name: '个人中心',
	url: '../' + localStorage.getItem('userTable') + '/center.html'
}, 
]


var indexNav = [

{
	name: '社会实践活动',
	url: './pages/shehuishijianhuodong/list.html'
}, 

{
	name: '系统公告',
	url: './pages/news/list.html'
},
]

var adminurl =  "http://localhost:8080/djangoa1c08/admin/dist/index.html";

var cartFlag = false

var chatFlag = false




var menu = [{"backMenu":[{"child":[{"buttons":["新增","查看","修改","删除"],"menu":"项目分类","menuJump":"列表","tableName":"xiangmufenlei"}],"menu":"项目分类管理"},{"child":[{"buttons":["新增","查看","修改","删除"],"menu":"学生","menuJump":"列表","tableName":"xuesheng"}],"menu":"学生管理"},{"child":[{"buttons":["新增","查看","修改","删除"],"menu":"教师","menuJump":"列表","tableName":"jiaoshi"}],"menu":"教师管理"},{"child":[{"buttons":["查看","修改","删除","审核","报表"],"menu":"学生活动申报","menuJump":"列表","tableName":"xueshenghuodongshenbao"}],"menu":"学生活动申报管理"},{"child":[{"buttons":["查看","修改","删除","审核","报表"],"menu":"社会实践活动","menuJump":"列表","tableName":"shehuishijianhuodong"}],"menu":"社会实践活动管理"},{"child":[{"buttons":["查看","修改","删除","报表"],"menu":"活动报名申请","menuJump":"列表","tableName":"huodongbaomingshenqing"}],"menu":"活动报名申请管理"},{"child":[{"buttons":["查看","修改","删除"],"menu":"轮播图管理","tableName":"config"},{"buttons":["新增","查看","修改","删除"],"menu":"系统公告","tableName":"news"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"buttons":["查看","报名"],"menu":"社会实践活动列表","menuJump":"列表","tableName":"shehuishijianhuodong"}],"menu":"社会实践活动模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"buttons":["新增","查看","修改","删除"],"menu":"学生活动申报","menuJump":"列表","tableName":"xueshenghuodongshenbao"}],"menu":"学生活动申报管理"},{"child":[{"buttons":["查看","删除"],"menu":"活动报名申请","menuJump":"列表","tableName":"huodongbaomingshenqing"}],"menu":"活动报名申请管理"}],"frontMenu":[{"child":[{"buttons":["查看","报名"],"menu":"社会实践活动列表","menuJump":"列表","tableName":"shehuishijianhuodong"}],"menu":"社会实践活动模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"学生","tableName":"xuesheng"},{"backMenu":[{"child":[{"buttons":["查看","修改","删除","审核"],"menu":"学生活动申报","menuJump":"列表","tableName":"xueshenghuodongshenbao"}],"menu":"学生活动申报管理"},{"child":[{"buttons":["新增","查看","修改","删除"],"menu":"社会实践活动","menuJump":"列表","tableName":"shehuishijianhuodong"}],"menu":"社会实践活动管理"},{"child":[{"buttons":["查看","修改","删除","审核"],"menu":"活动报名申请","menuJump":"列表","tableName":"huodongbaomingshenqing"}],"menu":"活动报名申请管理"}],"frontMenu":[{"child":[{"buttons":["查看","报名"],"menu":"社会实践活动列表","menuJump":"列表","tableName":"shehuishijianhuodong"}],"menu":"社会实践活动模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"教师","tableName":"jiaoshi"}]


var isAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].backMenu.length;j++){
                for(let k=0;k<menus[i].backMenu[j].child.length;k++){
                    if(tableName==menus[i].backMenu[j].child[k].tableName){
                        let buttons = menus[i].backMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}

var isFrontAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}
