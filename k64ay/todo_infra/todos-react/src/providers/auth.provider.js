import React, { createContext, useReducer, useEffect, useContext, useState } from "react";
import jwtDecode from "jwt-decode";

import api from "../utils/api";
import { getRefreshToken, removeRefreshToken, removeTokens, setTokens } from "../utils/token";

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
    reloadUser: async (authData) => { },
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
    const [timerId, setTimerId] = useState();
    const [state, dispatch] = useReducer(authReducer, initialState);

    async function refresh() {
        const { data } = await api.post('/auth/jwt/refresh/', {
            refresh: getRefreshToken()
        });
        setTokens(data);
        clearTimeout(timerId);
        const tid = setTimeout(refresh, 1000 * 60 * 4.5);
        setTimerId(tid);
    }

    async function manageTokens () {
        let isGuest = true;
        const refreshToken = getRefreshToken();

        if (refreshToken) {
            isGuest = false;
            const refreshData = jwtDecode(refreshToken);

            /* Refresh token is expired */
            if (refreshData.exp * 1000 < Date.now()) {
                removeRefreshToken();
            } else {
                dispatch({ type: LOGIN_SUCCESS, payload: {} });
                await refresh();
            }
        }

        if (isGuest) {
            dispatch({ type: LOGIN_SUCCESS, payload: null });
        }
    }

    useEffect(() => {
        manageTokens();
        // eslint-disable-next-line
    }, []);

    async function login(username, password) {
        const { data } = await api.post('/auth/jwt/create/', {
            username, password
        })
        console.log('login', data);
        setTokens(data);
        refresh();

        dispatch({
            type: LOGIN_SUCCESS,
            payload: {}
        });
    }

    function logout() {
        removeTokens()
        dispatch({ type: LOGOUT });
    }

    return (state.isFetching ? 'Fetching...' :
        <AuthContext.Provider
            value={{ ...state, login, logout }}
            {...props}
        />
    );
}
