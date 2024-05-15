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
    <h1 style="text-align:center;">Requests</h1>
    <!-- Display Available Carpools -->
    <div v-if="availableCarpools.length" style="background-color:  #fad3a5;">
      <h3>Carpool Requests</h3>
      <div v-for="carpool in availableCarpools" :key="carpool.id" class="user-box">
        <div class="user-details">
          <p>Passenger Name: {{ carpool.passengerName }}</p>
          <p>Route: {{ carpool.route }}</p>
          <p>Start: {{ carpool.start }}</p>
          <p>End: {{ carpool.end }}</p>
          <p>Date: {{ carpool.date }}</p>
          <p>Start Time: {{ carpool.time }}</p>
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
        <div class="user-actions">
          <button class="accept-btn" @click="accept(carpool)">Accept</button>
          <button class="reject-btn" @click="reject(carpool)">Reject</button>
        </div>
      </div>
    </div>
    <!-- Display Available Carpools -->
    <div v-if="availableDelivery.length" style="background-color:  #fad3a5;">
      <h3>Product Delivery Requests</h3>
      <div v-for="carpool in availableDelivery" :key="carpool.id"  class="user-box">
        <div class="user-details">
          <p>Passenger Name: {{ carpool.passengerName }}</p>
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
          <!-- Link to view driver's profile -->
          <a href="#" class="profile-link" @click="viewProfile(carpool)">View profile</a>
        </div>
        <div class="user-actions">
          <button class="accept-btn" @click="accept(carpool)">Accept</button>
          <button class="reject-btn" @click="reject(carpool)">Reject</button>
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
      errormessage: "",
    };
  },
  mounted() {
    this.searchCarpools();
    this.searchProduct();
  },
  methods: {
    searchCarpools() {
      axios.post('http://127.0.0.1:8000/search-request/')
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
      axios.get('http://127.0.0.1:8000/search-request/')
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
    accept(carpool)
    {
      axios.post('http://127.0.0.1:8000/accept-request/', carpool)
      .then(response => {
          console.log(response.data);
          this.searchProduct();
          this.searchCarpools();
        })
        .catch(error => {
          console.error('Error requesting carpool:', error);
          this.errormessage = "Error requesting product delivery";
        });
    },
    reject(carpool)
    {
      axios.post('http://127.0.0.1:8000/reject-request/', carpool)
      .then(response => {
          console.log(response.data);
          this.searchProduct();
          this.searchCarpools();
        })
        .catch(error => {
          console.error('Error requesting carpool:', error);
          this.errormessage = "Error requesting product delivery";
        });
    },
    viewProfile(carpool) {
        axios.post('http://127.0.0.1:8000/driver-id-save/', {driver_id: carpool.driver_id})
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
  .user-box {
  background-color: white;
  margin-bottom: 20px;
  margin-left:30px;
  display: flex;
  justify-content: space-between;
  padding: 20px;
  width: 1100px;
}

.user-actions {
  display: flex;
}

.accept-btn {
  background-color: green;
  color: white;
  margin-right: 10px;
}

.reject-btn {
  background-color: red;
  color: white;
}
</style>