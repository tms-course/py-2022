import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { useAuthContext } from '../providers/auth.provider';

export default function SharedLayout() {
    const { isAuthenticated, logout } = useAuthContext();

    return (
        <div className="container">
            <ul className="nav justify-content-end">
                {isAuthenticated ? (
                    <li className="nav-item">
                        <NavLink className="nav-link" onClick={logout}>Log out</NavLink>
                    </li>
                ) : (
                    <li className="nav-item">
                        <NavLink className="nav-link" to="login">Log in</NavLink>
                    </li>
                )}
            </ul>
            
            <Outlet />
        </div>
    );
}