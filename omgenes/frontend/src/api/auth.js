import api from "@/api/api.service";
import Cookies from 'js-cookie'

async function googleCallback(idToken){
    return api.post("google/verify-google-token/", {id_token: idToken})
}

async function fetchUser(){
    return api.post("google/fetch-user/", {token: Cookies.get('authtoken')})
}

export default {
    googleCallback, fetchUser
}