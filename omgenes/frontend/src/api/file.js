import api from "@/api/api.service";
import Cookies from 'js-cookie'

// Test endpoint
async function uploadFile(formData){
    // console.log("attempting upload")
    return api.post("files/upload/", formData)
}

// Variant Read endpoints
async function uploadProjectFile(formData){
    return api.post("files/uploadfile/", formData)
}

// Create new Variant Read Project
async function createReads(formData){
    return api.post("files/createproject/", formData)
}

// Update links for Variant Read
async function updateReadsLinks(formData){
    return api.patch("files/updateprojlinks/", formData)
}

// Fetch request for getting Variant Reads
async function fetchReads(){
    return api.post("files/fetchreads/", {token: Cookies.get('authtoken')})
}

// Fetch request for getting individual Reads
async function fetchRead(id){
    return api.post("files/fetchread/", {token: Cookies.get('authtoken'), readid: id})
}

// Fetch request for deleting an individual read
async function deleteRead(id){
    return api.post("files/deleteproject/", {token: Cookies.get('authtoken'), readid: id})
}

export default {
    uploadFile, createReads, fetchReads, fetchRead, uploadProjectFile, updateReadsLinks, deleteRead
}