import React from 'react';
import { createSearchParams, useLocation, Navigate, Outlet } from 'react-router-dom';

import { useAuthContext } from '../providers/auth.provider';

export function GuestRoute() {
    const { isAuthenticated } = useAuthContext();

    return isAuthenticated ? <Navigate to="/" /> : <Outlet />;
}

export function MemberRoute() {
    const { isAuthenticated } = useAuthContext();
    const location = useLocation();

    return isAuthenticated ? <Outlet /> : (
        <Navigate to={`/auth/login?${createSearchParams({ next: location.pathname })}`} />
    );
}

