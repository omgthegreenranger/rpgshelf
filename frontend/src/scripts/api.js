import axios from 'axios';


// const api_instance = axios.create({
//   baseURL: 'http://localhost:5000',
//   timeout: 1000,  
// })

const API_ENDPOINT = 'http://127.0.0.1:5000'

export async function api_call(search_term, search_result) {
    const search = search_result.split('_')[0];
    await axios.get(API_ENDPOINT + "/search?" + "search_type=" + search + "&search_string=" + search_term)
    .then(function (response) {
        console.log(response);
        return response;
    })
    .catch(function (error) {
        console.log(error);
    })
    .finally(function () {

    })
}