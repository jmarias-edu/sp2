import api from "@/api/api.service";

async function googleCallback(idToken){
    return api.post("google/verify-google-token/", {id_token: idToken})
}

export default {
    googleCallback
}