import React from 'react';
import { Link } from 'react-router-dom';
import './SignUp.css';

const handleSubmit = (event) => {
  event.preventDefault();
  const { email, password } = event.target.elements;
  console.log(email.value, password.value);
  // TODO: SIGN UP CODE HERE
}

export default function SignUp() {
  return (
    <div id="login-form-wrap">
      <h2>Sign Up</h2>
      <form id="login-form" onSubmit={handleSubmit}>
        <p>
          <input type="email" id="email" name="email" placeholder="Email Address" required /><i class="validation"><span></span><span></span></i>
        </p>
        <p>
          <input type="password" id="password" name="password" placeholder="Password" required /><i class="validation"><span></span><span></span></i>
        </p>
        <p>
          <input type="submit" id="signup" value="Sign Up" />
        </p>
      </form>
      <div id="create-account-wrap">
        <p>Already Registered? <Link to={"login"}>Login</Link></p>
      </div>
    </div>
  );
}
