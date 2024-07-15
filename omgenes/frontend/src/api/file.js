import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function uploadFile(formData){
    // console.log("attempting upload")
    return api.post("files/upload/", formData)
}

async function uploadProjectFile(formData){
    return api.post("files/uploadfile/", formData)
}

async function createReads(formData){
    return api.post("files/createproject/", formData)
}

async function updateReadsLinks(formData){
    return api.patch("files/updateprojlinks/", formData)
}

async function fetchReads(){
    return api.post("files/fetchreads/", {token: Cookies.get('authtoken')})
}

async function fetchRead(id){
    return api.post("files/fetchread/", {token: Cookies.get('authtoken'), readid: id})
}

async function deleteRead(id){
    return api.post("files/deleteproject/", {token: Cookies.get('authtoken'), readid: id})
}

export default {
    uploadFile, createReads, fetchReads, fetchRead, uploadProjectFile, updateReadsLinks, deleteRead
}