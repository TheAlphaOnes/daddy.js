
import { daddy } from "http://daddyjs.vercel.app/cdn/daddy.js";

let data = {"12a":"gg1","12b":"gg2"}
let alernate_data = [["gg1","alternate gg1"],["gg2","alternate gg2"]]
daddy("https://daddyjstest.netlify.app",data,alernate_data)

