import m from "mithril"
import { Posts } from "./models/Posts"

export const App = {
    oninit: Posts.loadList,
    view: ({ attrs: { state, actions } }) => [
        m("h3", "trying to access the API"),
        m("ul", Posts.list.map(function(post) {
            return m("li", post.title)
        }))
    ]
}
