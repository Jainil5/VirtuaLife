import React from 'react';
import { Link } from 'react-router-dom';
import './SignUp.css';

const handleSubmit = (event) => {
    event.preventDefault();
    const { email, password } = event.target.elements;
    console.log(email.value, password.value);
    // TODO: LOGIN CODE HERE
}

export default function Login() {
    return (
        <div id="login-form-wrap">
            <h2>Login</h2>
            <form id="login-form" onSubmit={handleSubmit}>
                <p>
                    <input type="email" id="email" name="email" placeholder="Email Address" required /><i class="validation"><span></span><span></span></i>
                </p>
                <p>
                    <input type="password" id="password" name="password" placeholder="Password" required /><i class="validation"><span></span><span></span></i>
                </p>
                <p>
                    <input type="submit" id="login" value="Login" />
                </p>
            </form>
            <div id="create-account-wrap">
                <p>Not Registered? <Link to={"sign-up"}>Sign up</Link></p>
            </div>
        </div>
    );
}
