<template>
  <div id="AdminPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 150vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <p style="cursor: pointer; margin-left: 1000px;" @click="carpool" ><u>ID proof</u></p>
      <p style="cursor: pointer; " @click="driving_license" ><u>Driving license</u></p>
      <p style="cursor: pointer;" @click="signout" ><u>Sign out</u></p>
      <p style="cursor: pointer;" @click="aboutUs"><u>About Us</u></p>
    </header>
    <p></p>
    <h2>Created Carpools</h2>
    <!-- Display Available Carpools -->
    <div v-if="availableCarpools.length">
      <div v-for="carpool in availableCarpools" :key="carpool.id" class="carpool-box">
        <!-- Carpool details -->
        <div>
          <p><strong>Driver Name: </strong>{{ carpool.driverName }}</p>
          <p><strong>Route: </strong>{{ carpool.route }}</p>
          <p><strong>Vehicle Type: </strong>{{ carpool.vehicle_type }}</p>
          <p><strong>Vehicle Model: </strong>{{ carpool.vehicle_model }}</p>
          <p><strong>Seats: </strong>{{ carpool.availableSeats }} out of {{ carpool.totalSeats }}</p>
          <p><strong>Date: </strong>{{ carpool.date }}</p>
          <p><strong>Start Time: </strong>{{ carpool.time }}</p>
          <p><strong>Price: </strong>{{ carpool.price }}</p>
          <!-- Display preferences with glowing objects based on driver preferences -->
          <label><strong>Preferences</strong></label>
          <div>
            <span v-if="carpool.smoking">🚬</span>
            <span v-if="carpool.chit_chat">💬</span>
            <span v-if="carpool.eat_drink">🍔🥤</span>
            <span v-if="carpool.pets">🐶</span>
            <span v-if="carpool.music">🎵</span>
            <span v-if="carpool.ac">❄️</span>
          </div>
          <div v-if="carpool.productDelivery">
            <p><strong>Product Delivery: </strong>{{ carpool.productDelivery }}</p>
            <p><strong>Delivery Price: </strong>{{ carpool.deliveryPrice }}</p>
          </div>
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
      </div>
    </div>
    <p v-if="this.errormessage" style="color: red;">{{ this.errormessage }}</p>
  </div>
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
      availableCarpools: [],
      errormessage: "",
    };
  },
  mounted()
  {
    this.searchCarpools();
  },
  methods: {
    searchCarpools() {
      axios.post('http://127.0.0.1:8000/admin-created-carpool/')
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
    signout()
      {
        this.$router.push({ name: 'StPage' });
      },
    carpool()
    {
      this.$router.push({ name: 'AdminPage' });
    },
    aboutUs() {
        this.$router.push({ name: 'AboutUs' });
      },
    driving_license(){
      this.$router.push({ name: 'DrivingLicense' });
    }
  }
};
</script>

<style>
  .carpool-box {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    width: 1100px;
    margin-left:30px;
  }

  .profile-link {
    color: blue;
    text-decoration: underline;
  }

  .main {
    --color-navajowhite: #fad3a5;
    background-color: var(--color-navajowhite);
  }
</style>