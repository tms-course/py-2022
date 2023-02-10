const TOKEN_KEY = 'token'

export const getToken = () => (localStorage.getItem(TOKEN_KEY));
export const setToken = (value) => localStorage.setItem(TOKEN_KEY, value);
export const removeToken = () => { console.log('removing'); localStorage.removeItem(TOKEN_KEY) };