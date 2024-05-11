import api from "@/api/api.service";

async function googleCallback(idToken){
    console.log("In auth: ", idToken)
    return api.post("google/verify-google-token/", {id_token: idToken})
}

export default {
    googleCallback
}