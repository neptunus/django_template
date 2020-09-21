import m from "mithril"

export const Posts = {
    list: [],
    loadList: function() {
        return m.request({
            method: "GET",
            url: "/posts/",
            withCredentials: true
        })
        .then(function(result) {
            Posts.list = result
        })
    }
}
