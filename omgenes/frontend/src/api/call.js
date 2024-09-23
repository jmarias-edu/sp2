import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function createCall(formData){
    return api.post("files/createcall", formData)
}

async function uploadCallFile(formData){
    return api.post("files/uploadcallfile", formData)
}

export default {
    createCall, uploadCallFile
}