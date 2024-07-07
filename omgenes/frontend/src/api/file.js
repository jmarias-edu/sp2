import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function uploadFile(formData){
    // console.log("attempting upload")
    return api.post("files/upload/", formData)
}

async function createReads(formData){
    
    console.log(formData)
    return api.post("files/createproject/", formData)
}

export default {
    uploadFile, createReads
}