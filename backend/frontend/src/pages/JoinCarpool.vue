<template>
  <div id="SignUpPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 150vh;">
    <!-- Header Section -->
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color: #fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer; margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
        <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
        <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
      </div>
    </header>

    <!-- Main Content Section -->
    <div style="padding: 20px;">
      <h1 style="text-align: center;">Join Carpool</h1>
      <div class="input-box">
        <div>
          <label>Date:</label>
          <input type="date" v-model="date" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px; width:200px; margin-left: 73px; background-color: #FBAF56;">
        </div>
        <div>
          <label>Start Location:</label>
          <input type="text" v-model="startLocation" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 12px; background-color: #FBAF56;">
        </div>
        <div>
          <label>End Location:</label>
          <input type="text" v-model="endLocation" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 16px; background-color: #FBAF56;">
        </div>
        <button @click="searchCarpools" style="border-radius: 20px; width: 400px; height: 40px; background-color: #FBAF56; font-weight: bold; border-color: white;">Search</button>
      </div>

      <!-- Display Available Carpools -->
      <div v-if="availableCarpools.length" style="background-color: #fad3a5; padding: 20px; margin-top: 20px;">
        <h3>Available Carpools</h3>
        <div v-for="carpool in availableCarpools" :key="carpool.id" class="carpool-box">
          <!-- Carpool Information -->
          <div class="carpool-info">
            <!-- Display carpool information -->
          </div>
          <!-- Button Container -->
          <div class="button-container">
            <!-- Link to view driver's profile -->
            <p class="profile-link" @click="view_profile(carpool.user_id)">View profile</p>
            <button class="request-button" @click="request(carpool)">Request</button>
          </div>
        </div>
      </div>
      <!-- Error Message -->
      <p v-if="errormessage" style="color: red;">{{ errormessage }}</p>
    </div>

    <!-- Footer Section -->
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
      date: '',
      startLocation: '',
      endLocation: '',
      availableCarpools: [],
      errormessage: "",
    };
  },
  methods: {
    searchCarpools() {
      axios.post('http://127.0.0.1:8000/search-carpool/', {date: this.date,start_location: this.startLocation,end_location: this.endLocation})
      .then(({data}) => {
    console.log("Received data from backend:", data);
    if (Array.isArray(data)) {
      this.availableCarpools = data;
    } else {
      this.errormessage = data; // Display error message if no rides are available
    }
  })
  .catch(error => {
    console.error('Error fetching carpools:', error);
    this.errormessage = "Error fetching carpools";
  });
    },
    request(carpool)
    {
      axios.post('http://127.0.0.1:8000/request-carpool/', {date: this.date,start_location: this.startLocation,end_location: this.endLocation, carpool_id: carpool.id, driver_id: carpool.user_id, price: carpool.price})
      this.searchCarpools();
    },
    view_profile(user_id)
    {
      this.$router.push({ name: 'ViewProfile', params: { userId: user_id } });
    },
    aboutUs() {
      this.$router.push({ name: "AboutUs" });
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

<style>
  .input-box{
    background-color:rgba(255, 255, 255, 0.4);
    border: 1px rgba(255, 255, 255, 0.4);
    border-radius: 10px;
    padding: 20px;
    margin: 20px;
  }
  .profile-link {
    color: blue;
    text-decoration: underline;
  }
  .footerComponent {
    background: linear-gradient(90deg, #fb0f72, #f9a84a);
    padding: 20px;
    text-align: center;
    color: white;
  }
  .header-links {
    display: flex;
    align-items: center;
  }
  .carpool-box {
    border: 1px solid black;
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    display: flex;
    justify-content: space-between;
  }
  .carpool-info {
    flex: 1;
  }
  .button-container {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }
  .request-button {
    margin-top: 10px;
    align-items: left;
  }
</style>
