<template>
  <div class="main" id="SignUpPage" style="background-color:  #fad3a5; display: flex; flex-direction: column; height: 90vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
        <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
        <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
      </div>
    </header>
    <p></p>
    <p></p>
    <div class="row" v-if="driving_license">
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="create_carpool()">Create Carpool</button>
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="request()">Requests</button>
    </div>
    <div class="row">
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="join_carpool()">Join Carpool</button>
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="product_delivery()">Product Delivery</button>
    </div>
    <div class="row">
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="cancel_request()">Cancel Carpool/Requests</button>
      <button style="font-weight: bold; border-color: #fad3a5; border-radius: 30px; height: 60px; width: 200px; background-color:#F668A4;" @click="request_status()">Request Status</button>
    </div>
  </div>
  <footer class="footerComponent">
    <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
    </footer>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      driving_license:null
    };
  },
  mounted(){
    axios.get("http://127.0.0.1:8000/check-driver/")
        .then(response => {
          console.log(response.data);
          this.driving_license=response.data.driving_license;
        })
        .catch(error => {
          console.error(error);
        });
  },
  methods: {
    aboutUs() {
      this.$router.push({ name: 'AboutUs' });
    },
    onButton1Container1Click() {
      this.$router.push("/your-profile");
    },
    create_carpool() {
      this.$router.push({ name: 'CreateCarpoolPage' });
    },
    join_carpool() {
      this.$router.push({ name: 'JoinCarpool' });
    },
    product_delivery() {
      this.$router.push({ name: 'SearchPdtDelivery' });
    },
    cancel_request() {
      this.$router.push({ name: 'Cancel' });
    },
    request() {
      this.$router.push({ name: 'RequestTable' });
    },
    request_status() {
      this.$router.push({ name: 'RequestStatus' });
    },
    signOut() {
      this.$router.push({ name: "StPage" });
    },
    goToMyProfile() {
      this.$router.push({ name: "YourProfile" });
    }
  }
};
</script>

<style scoped>
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.row {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.row button {
  margin: 0 10px; /* Adjust the gap between buttons */
}
</style>
