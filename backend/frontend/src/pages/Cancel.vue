<template>
  <div style="background-color: #fad3a5; display: flex; flex-direction: column; height: 100vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
      <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
      <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
      <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
    </div>
    </header>
    <h1 style="text-align: center;">Cancellation</h1>
    <!-- Display Available Carpools -->
    <div v-if="availableCarpools.length" style="background-color: #fad3a5;">
      <h3>Cancel Joined Carpool</h3>
      <div v-for="carpool in availableCarpools" :key="carpool.id" class="carpool-box">
        <div class="user-details">
          <p>Driver Name: {{ carpool.driverName }}</p>
          <p>Route: {{ carpool.route }}</p>
          <p>Start: {{ carpool.start }}</p>
          <p>End: {{ carpool.end }}</p>
          <p>Date: {{ carpool.date }}</p>
          <p>Start Time: {{ carpool.time }}</p>
          <p>Status: {{ carpool.status }}</p>
          <p>Price: {{ carpool.price }}</p>
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
        <div class="button">
          <button class="cancel-button" @click="cancel(carpool)">Cancel</button>
        </div>
      </div>
    </div>
    <!-- Display Available Carpools -->
    <div v-if="availableDelivery.length" style="background-color: #fad3a5;">
      <h3>Cancel Product Delivery</h3>
      <div v-for="carpool in availableDelivery" :key="carpool.id" class="carpool-box">
        <div class="user-details">
          <p>Driver Name: {{ carpool.driverName }}</p>
          <p>Route: {{ carpool.route }}</p>
          <p>Start: {{ carpool.start }}</p>
          <p>End: {{ carpool.end }}</p>
          <p>Date: {{ carpool.date }}</p>
          <p>Start Time: {{ carpool.time }}</p>
          <p>Product weight: {{ carpool.wgt }}</p>
          <p>Product size: {{ carpool.size }}</p>
          <p>Product type: {{ carpool.type }}</p>
          <div v-if="carpool.anyother">
            <p>Product weight: {{ carpool.anyother }}</p>
          </div>
          <p>Status: {{ carpool.status }}</p>
          <p>Price: {{ carpool.price }}</p>
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
        <div class="button">
          <button class="cancel-button"@click="cancel(carpool)">Cancel</button>
        </div>
      </div>
    </div>
    <div v-if="CreatedCarpool.length" style="background-color: #fad3a5;">
      <h3>Cancel created Carpool</h3>
      <div v-for="carpool in CreatedCarpool" :key="carpool.id" class="carpool-box"> 
        <div class="user-details">
          <p>Route: {{ carpool.route }}</p>
          <p>Start: {{ carpool.start }}</p>
          <p>End: {{ carpool.end }}</p>
          <p>Date: {{ carpool.date }}</p>
          <p>Start Time: {{ carpool.time }}</p>
          <p>Price: {{ carpool.price }}</p>
        </div>
        <div class="button">
          <button class="cancel-button" @click="cancel(carpool)">Cancel</button>
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
      availableDelivery: [],
      availableCarpools: [],
      CreatedCarpool: [],
      errormessage: "",
    };
  },
  mounted(){
    this.searchCarpools();
    this.searchCreatedCarpool();
    this.searchProduct();
  },
  methods: {
    searchCarpools() {
      axios.post('http://127.0.0.1:8000/cancel-content/')
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
    searchProduct() {
      axios.get('http://127.0.0.1:8000/cancel-content/')
      .then(({data}) => {
    console.log("Received data from backend:", data);
    if (Array.isArray(data)) {
      this.availableDelivery = data;
    } else {
      this.errormessage = data.message; // Display error message if no rides are available
    }
  })
  .catch(error => {
    console.error('Error fetching carpools:', error);
    this.errormessage = "Error fetching carpools";
  });
    },
    cancel(carpool)
    {
      axios.post('http://127.0.0.1:8000/cancel/', carpool)
      .then(response => {
          console.log(response.data);
          this.availableCarpools=[];
          this.availableDelivery=[];
          this.CreatedCarpool=[];
          this.searchProduct();
          this.searchCarpools();
          this.searchCreatedCarpool();
        })
        .catch(error => {
          console.error('Error requesting carpool:', error);
          this.errormessage = "Error requesting product delivery";
        });
    },
    searchCreatedCarpool() {
      axios.put('http://127.0.0.1:8000/cancel-content/')
      .then(({data}) => {
    console.log("Received data from backend:", data);
    if (Array.isArray(data)) {
      this.CreatedCarpool = data;
    } else {
      this.errormessage = data.message; 
    }
  })
  .catch(error => {
    console.error('Error fetching carpools:', error);
    this.errormessage = "Error fetching carpools";
  });
    },
    viewProfile(carpool) {
        axios.post('http://127.0.0.1:8000/driver-id-save/', {driver_id: carpool.id})
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "ViewProfile" });
        })
        .catch(error => {
          console.error('Error viewing profile:', error);
          this.errormessage = "Error viewing profile";
        });
    },
  }
};
</script>
<style>
    .profile-link {
        color: blue;
        text-decoration: underline;
    }

    .cancel-button{
      background-color: lightpink;
      color: black;
      margin-right: 10px;
    }

    .user-box {
      background-color: white;
      margin-bottom: 20px;
      margin-left:30px;
      display: flex;
      justify-content: space-between;
      padding: 20px;
      width: 1100px;
    }

    .button{
      display: flex;
    }
</style>