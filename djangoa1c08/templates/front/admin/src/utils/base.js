const base = {
    get() {
        return {
            url : "http://localhost:8080/djangoa1c08/",
            name: "djangoa1c08",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "大学生社会实践申报系统的设计与实现"
        } 
    }
}
export default base
