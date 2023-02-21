import axios from "axios";
import { API_URL } from "../config";
import { getAccessToken } from "./token";


const axiosInstance = axios.create({
    baseURL: API_URL,
    // timeout: 5000,
    responseType: 'json',
    responseEncoding: 'utf8',
});

axiosInstance.interceptors.request.use(config => {
    const token = getAccessToken();

    if (token) {
        config.headers.Authorization = `JWT ${token}`;
    }

    return config;
});

export default axiosInstance;