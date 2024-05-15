<template>
  <div id="CreateCarpoolPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 100vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
      </div>
    </header>
    <div class="main-content" style="flex-grow: 1; display: flex;">
      <div class="container" style="flex-grow: 1; display: flex; justify-content: flex-start; align-items: center; background-image: url(/rectangle-17@2x.png); background-size: cover; background-position: center; background-repeat: no-repeat;">
        <div class="form-container" style="height:250px; padding: 20px; border: 1px rgba(255, 255, 255, 0.98); border-radius: 10px; background-color: rgba(255, 255, 255, 0.75);">
          <h1 style="text-align: center;">Login</h1>
          <form @submit.prevent="submit">
            <div>
              <label for="email" style="margin-right: 32px;">Email:</label>
              <input type="email" id="email" v-model="login.email" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 20px; margin-bottom: 10px;">
            </div>
            <div>
              <label for="password" style="margin-right: 10px;">Password:</label>
              <input type="password" id="password" v-model="login.password" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5);  height: 20px; margin-bottom: 10px;">
            </div>
            <p style="text-align: center;"@click="forget_pwd">Forget password? Click here</p>
            <button type="submit" style="background-color: orange; width:150px; border-radius: 20px; height:30px; border-color: rgba(255, 255, 255, 0.5);">Login</button>
          </form>
          <p v-if="login.errormessage" style="color: red;">{{ login.errormessage }}</p>
        </div>
      </div>
    </div>
  </div>
  <footer class="footerComponent">
    <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
  </footer>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      login: {
        email: "",
        password: "",
        errormessage: ""
      }
    };
  },
  methods: {
    forget_pwd() {
      this.$router.push({ name: "ForgotPassword" });
    },
    submit() {
      axios.post("http://127.0.0.1:8000/Login/", this.login)
        .then(response => {
          console.log(response.data);
          if (response.data.message == "login successful") {
            // Redirect to Home Page
            this.$router.push({ name: "HomePage" });
          } else if (response.data.message == "not verified") {
            this.$router.push({ name: "ProfileNotVerified" });
          } else if (response.data.message == "admin login successful") {
            this.$router.push({ name: "AdminPage" });
          } else {
            this.login.errormessage = response.data.message;
          }
        })
        .catch(error => {
          console.error(error);
          this.login.errormessage = "An error occurred during login.";
        });
    },
    aboutUs() {
      this.$router.push({ name: "AboutUs" });
    }
  }
};
</script>

<style>
#LoginPage {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main-content {
  flex-grow: 1;
}

.container {
  flex-grow: 1;
}

.form-container {
  padding: 20px;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  max-width: 60%;
}
</style>

