import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function uploadFile(formData){
    console.log("attempting upload")
    return api.post("files/upload/", formData, 
    {headers: {
        'Content-Type': 'multipart/form-data',
      }, token: Cookies.get('authtoken')
    })
}

export default {
    uploadFile,
}