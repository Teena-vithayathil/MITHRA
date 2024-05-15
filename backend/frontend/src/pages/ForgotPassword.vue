<template>
  <div id="AdminPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 100vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <p style="cursor: pointer;" @click="aboutUs"><u>About Us</u></p>
    </header>
    <p></p>
    <h1 style="text-align:center; margin-bottom: 20px;">Forget Password</h1>
    <div style="text-align:center; margin-bottom: 10px;">
      <label>Email:</label>
      <input type="email" v-model="email" required>
    </div>
    <div style="text-align:center; margin-bottom: 10px;">
      <label>New Password:</label>
      <input type="password" v-model="password" required>
    </div>
    <div style="text-align:center; margin-bottom: 10px;">
      <label>Retype Password:</label>
      <input type="password" v-model="retypePassword" required>
    </div>
    <button @click="resetPassword" style="margin-bottom: 10px;">Submit</button>
    <p v-if="errorMessage" style="color: red; text-align:center;">{{ errorMessage }}</p>
    <p v-if="noerrorMessage" style="color: green; text-align:center;">{{ noerrorMessage }}</p>

  </div>
  <footer class="footerComponent">
    <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
  </footer>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      retypePassword: '',
      errorMessage: '',
      noerrorMessage: ''
    };
  },
  methods: {
    resetPassword() {
      // Basic form validation
      if (!this.email || !this.password || !this.retypePassword) {
        this.errorMessage = 'All fields are required.';
        return;
      }
      if (this.password !== this.retypePassword) {
        this.errorMessage = 'Passwords do not match.';
        return;
      }

      // Reset password logic
      axios.post('http://127.0.0.1:8000/forgot-password/', {
        email: this.email,
        password: this.password,
        re_password: this.retypePassword
      })
      .then(response => {
        this.errorMessage = "";
        console.log(response.data);
        this.noerrorMessage = "Password changed";
        this.email = ''; // Clear email field
        this.password = ''; // Clear password field
        this.retypePassword = ''; // Clear retype password field
        this.$router.push({ name: 'LoginPage' });
      })
      .catch(error => {
        // Handle error
        console.error('Error resetting password:', error);
        this.errorMessage = 'Invalid email id.';
      });
    },
    aboutUs() {
        this.$router.push({ name: 'AboutUs' });
      }
  }
};
</script>

<style>
  /* Add your CSS styles here */
</style>

