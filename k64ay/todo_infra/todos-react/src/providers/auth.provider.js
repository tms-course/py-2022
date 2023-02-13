import React, { createContext, useReducer, useEffect, useContext } from "react";
// import jwtDecode from "jwt-decode";

// import api from "../utils/api";
import { getToken, removeToken, setToken } from "../utils/token";

const LOGIN_FETCHING = 'LOGIN_FETCHING';
const LOGIN_SUCCESS = 'LOGIN_SUCCESS';
const LOGOUT = 'LOGOUT';

let initialState = {
    isFetching: true,
    isAuthenticated: false,
    // user: null
};

export const AuthContext = createContext({
    isAuthenticated: false,
    // user: null,
    login: (data) => { },
    logout: () => { },
    reloadUser: async (token) => { },
});

export function useAuthContext() {
    return useContext(AuthContext);
}

function authReducer(state, action) {
    switch (action.type) {
        case LOGIN_FETCHING:
            return {
                ...state,
                isFetching: true
            };
        case LOGIN_SUCCESS:
            return {
                ...state,
                isFetching: false,
                isAuthenticated: !!action.payload,
                // user: action.payload
            };
        case LOGOUT:
            return {
                ...state,
                isAuthenticated: false,
                // user: null
            };
        default:
            return state;
    }
}

export function AuthProvider(props) {
    const [state, dispatch] = useReducer(authReducer, initialState);

    useEffect(() => {
        let isGuest = true;
        const token = getToken();

        if (token) {
            isGuest = false;
            reloadUser(token);
            // const decoded = jwtDecode(token);

            // if (decoded.exp * 1000 < Date.now()) {
            //     console.log('removing expired token');
            //     removeToken()
            // } else {
            //     if (!state.user) {
            //         isGuest = false;
            //         reloadUser();
            //     }
            // }
        }

        if (isGuest) {
            dispatch({ type: LOGIN_SUCCESS, payload: null });
        }
        // eslint-disable-next-line
    }, []);

    async function reloadUser(token) {
        if (token) {
            setToken(token);
        }

        dispatch({ type: LOGIN_FETCHING })
        //const {data:res} = await api.get('/me');        
        login({});
    }

    function login(userData = {}) {
        dispatch({
            type: LOGIN_SUCCESS,
            payload: userData
        });
    }

    function logout() {
        removeToken()
        dispatch({ type: LOGOUT });
    }

    return (state.isFetching ? 'Fetching...' :
        <AuthContext.Provider
            value={{ ...state, login, logout, reloadUser }}
            {...props}
        />
    );
}
