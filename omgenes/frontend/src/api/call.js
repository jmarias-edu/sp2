import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function createCall(formData){
    return api.post("files/createcall/", formData)
}

async function uploadCallFile(formData){
    return api.post("files/uploadcallfile/", formData)
}

async function updateCallFile(formData){
    return api.patch("files/updatecalllinks/", formData)
}

async function fetchCalls(){
    return api.post("files/fetchcalls/", {token: Cookies.get('authtoken')})
}

async function fetchCall(id){
    return api.post("files/fetchcall/", {token: Cookies.get('authtoken'), callid: id})
}

async function deleteCall(id){
    return api.post("files/deletecall/", {token: Cookies.get('authtoken'), callid: id})
}

export default {
    createCall, uploadCallFile, updateCallFile, fetchCalls, fetchCall, deleteCall
}