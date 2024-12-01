import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function fetchAllReads(){
    return api.post("files/fetchAllReads/", {token: Cookies.get('authtoken')})
}

async function fetchAllCalls(){
    return api.post("files/fetchAllCalls/", {token: Cookies.get('authtoken')})
}

async function fetchAllUsers(){
    return api.post("files/fetchAllUsers/", {token: Cookies.get('authtoken')})
}

async function deleteUser(id){
    return api.post("google/delete-user/", {token: Cookies.get('authtoken'), todelete: id})
}

export default {
    fetchAllReads, fetchAllCalls, fetchAllUsers, deleteUser
}