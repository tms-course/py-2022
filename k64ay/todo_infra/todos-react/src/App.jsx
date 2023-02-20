import React from "react";
import {
    BrowserRouter as Router,
    Route,
    Routes
} from "react-router-dom";

import { AuthProvider } from "./providers/auth.provider";
import { GuestRoute, MemberRoute } from './utils/routing.utils';
import SharedLayout from "./components/SharedLayout";
import TodoContainer from "./pages/TodoContainer";
import LoginContainer from './pages/LoginContainer';


export default function App() {
    return (
        <AuthProvider>
            <Router basename='/'>
                <Routes>
                    <Route path="/" element={<SharedLayout />}>
                        <Route path="" element={<MemberRoute />}>
                            <Route index element={<TodoContainer />} />
                        </Route>
                        
                        <Route path="auth" element={<GuestRoute />}>
                            <Route path="login" element={<LoginContainer />} />
                        </Route>
                    </Route>
                </Routes>
            </Router>
        </AuthProvider>
    );
}
