const ACCESS_TOKEN_KEY = 'access_token'
const REFRESH_TOKEN_KEY = 'refresh_token'

export const getAccessToken = () => (localStorage.getItem(ACCESS_TOKEN_KEY));
export const getRefreshToken = () => (localStorage.getItem(REFRESH_TOKEN_KEY))
export const setAccessToken = (value) => localStorage.setItem(ACCESS_TOKEN_KEY, value);
export const setRefreshToken = (value) => localStorage.setItem(REFRESH_TOKEN_KEY, value);
export const setTokens = ({ access, refresh }) => {
    setAccessToken(access);
    setRefreshToken(refresh);
}
export const removeTokens = () => {
    removeAccessToken();
    removeRefreshToken();
}
export const removeAccessToken = () => localStorage.removeItem(ACCESS_TOKEN_KEY);
export const removeRefreshToken = () => localStorage.removeItem(REFRESH_TOKEN_KEY);