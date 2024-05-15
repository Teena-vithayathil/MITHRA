<template>
  <div id="SignUpPage" style="background-color:  #fad3a5; display: flex; flex-direction: column; height: 150vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
        <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
        <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
      </div>
    </header>
    <h1 style="text-align:center;">Product Delivery</h1>
    <div class="content-box">
      <div>
        <label>Date:</label>
        <input type="date" v-model="date" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 180px; background-color: #FBAF56;">
      </div>
      <div>
        <label>Start Location:</label>
        <input type="text" v-model="startLocation" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 120px; background-color: #FBAF56;">
      </div>
      <div>
        <label>End Location:</label>
        <input type="text" v-model="endLocation" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 125px; background-color: #FBAF56;">
      </div>
      <div>
        <label>Product length:</label>
        <input type="number" v-model="pro_size" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 120px; background-color: #FBAF56;">
      </div>
      <div>
        <label>Product weight:</label>
        <input type="number" v-model="pro_wgt" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 115px; background-color: #FBAF56;">
      </div>
      <div>
        <label>Product type:</label>
        <input type="text" v-model="pro_type" required style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 130px; background-color: #FBAF56;">
      </div>
      <div>
        <label>Product specification (optional):</label>
        <input type="text" v-model="pro_anyother" style="margin-bottom: 10px; border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); width:200px; height: 30px; margin-left: 10px; background-color: #FBAF56;">
      </div>
      <button @click="searchCarpools" style="border-radius: 20px; width: 400px; height: 40px; background-color: #FBAF56; font-weight: bold; border-color: white;">Search</button>
    </div>

    <!-- Display Available Carpools -->
    <div v-if="availableCarpools.length" style="background-color:  #fad3a5">
      <h3>Available Carpools</h3>
      <div v-for="carpool in availableCarpools" :key="carpool.id" class="carpool-box">
        <div class="carpool-info">
          <p>Driver Name: {{ carpool.driverName }}</p>
          <p>Route: {{ carpool.route }}</p>
          <p>Vehicle Type: {{ carpool.vehicle_type }}</p>
          <p>Vehicle Model: {{ carpool.vehicle_model }}</p>
          <p>Date: {{ carpool.date }}</p>
          <p>Start Time: {{ carpool.time }}</p>
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
        <div class="button">
          <button class="request-button" @click="request(carpool)">Request</button>
        </div>
      </div>
    </div>
    <p v-if="this.errormessage" style="color: red;">{{ this.errormessage }}</p>
  </div>
  <footer class="footerComponent">
      <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
    </footer>
</template>


<script>
import axios from 'axios';

export default {
  props: ['driverParams'],
  data() {
    return {
      date: '',
      startLocation: '',
      endLocation: '',
      pro_size: 0,
      pro_wgt: 0,
      pro_type: '',
      pro_anyother: '',
      availableCarpools: [],
      errormessage: "",
    };
  },
  methods: {
    searchCarpools() {
      axios.post('http://127.0.0.1:8000/search-product-delivery/', {date: this.date,start_location: this.startLocation,end_location: this.endLocation})
      .then(({data}) => {
    console.log("Received data from backend:", data);
    if (Array.isArray(data)) {
      this.availableCarpools = data;
    } else {
      this.errormessage = data.message; // Display error message if no rides are available
    }
  })
  .catch(error => {
    console.error('Error fetching carpools:', error);
    this.errormessage = "Error fetching carpools";
  });
    },
    request(carpool)
    {
      axios.post('http://127.0.0.1:8000/request-product-delivery/', {price:carpool.price,carpool_id: carpool.id,start_location: this.startLocation,end_location: this.endLocation,driver_id: carpool.user_id,pro_size: this.pro_size,pro_wgt: this.pro_wgt,pro_type: this.pro_type,pro_anyother: this.pro_anyother})
      .then(response => {
          console.log(response.data);
          this.availableCarpools=[];
          this.searchCarpools();
        })
        .catch(error => {
          console.error('Error requesting carpool:', error);
          this.errormessage = "Error requesting product delivery";
        });
    },
    viewProfile(carpool) {
        axios.post('http://127.0.0.1:8000/driver-id-save/', {driver_id: carpool.user_id})
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "ViewProfile" });
        })
        .catch(error => {
          console.error('Error viewing profile:', error);
          this.errormessage = "Error viewing profile";
        });
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
  .content-box {
    background-color:rgba(255, 255, 255, 0.4);
    border: 1px rgba(255, 255, 255, 0.4);
    border-radius: 10px;
    padding: 20px;
    margin: 20px;
  }
  .carpool-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .carpool-details {
    flex: 1;
  }
  .request-button {
    background-color:orange;
    color: black;
    margin-left: 10px;
  }
</style>