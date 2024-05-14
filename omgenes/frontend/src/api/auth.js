import api from "@/api/api.service";

async function googleCallback(idToken){
    return api.post("google/verify-google-token/", {id_token: idToken})
}

async function fetchUser(){
    return api.post("google/fetch-user/", {dummy: "dummy"})
}

export default {
    googleCallback, fetchUser
}