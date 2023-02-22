import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useAuthContext } from '../providers/auth.provider';


const Login = () => {
    const navigate = useNavigate();
    const { login } = useAuthContext();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    async function handleSubmit(event) {
        event.preventDefault();

        await login(username, password);
        navigate('/');
    }

    return (
        <form onSubmit={handleSubmit}>
            <h3>Sign In</h3>
            <div className="mb-3">
                <label>Username</label>
                <input
                    type="username"
                    className="form-control"
                    placeholder="Enter username"
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                />
            </div>
            <div className="mb-3">
                <label>Password</label>
                <input
                    type="password"
                    className="form-control"
                    placeholder="Enter password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />
            </div>
            <div className="d-grid">
                <button type="submit" className="btn btn-primary">
                    Submit
                </button>
            </div>
        </form>
    )
}

export default Login;
