<template>
  <div id="CreateCarpoolPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 180vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
      <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
      <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
      <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
    </div>
    </header>
    <h1 style="text-align: center;">Create Carpool</h1>
    <div class="container" style="flex-grow: 1; display: flex; justify-content: left ; align-items: center; ">
      <div class="form-container" style="padding: 20px; border: 1px rgba(255, 255, 255, 0.75); border-radius: 10px; background-color: white;max-width: 500px;">
    
    <div style="margin-bottom: 10px;">
        <label for="date">Date:</label>
        <input type="date" id="date" v-model="carpool.date" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px; margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="startTime">Start Time:</label>
        <input type="time" id="startTime" v-model="carpool.startTime" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px; margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="startLocation">Start Location:</label>
        <input type="text" id="startLocation" v-model="carpool.startLocation" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="endLocation">End Location:</label>
        <input type="text" id="endLocation" v-model="carpool.endLocation" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="viaRoute">Via Route:</label>
        <input type="text" id="viaRoute" v-model="carpool.viaRoute" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="vehicleType">Vehicle Type:</label>
        <input type="text" id="vehicleType" v-model="carpool.vehicleType" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="vehicleNo">Vehicle Number:</label>
        <input type="text" id="vehicleNo" v-model="carpool.vehicleNo" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="vehicleModel">Vehicle Model:</label>
        <input type="text" id="vehicleModel" v-model="carpool.vehicleModel" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="seatsAvailable">Seats Available:</label>
        <input type="number" id="seatsAvailable" v-model="carpool.seatsAvailable" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label for="Price">Price:</label>
        <input type="number" id="price" v-model="carpool.price" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px;  margin-left: 10px; background-color: #FBAF56;">
      </div>
      <div style="margin-bottom: 10px;">
        <label>Preferences:</label><br>
        <input type="checkbox" v-model="carpool.music">Music<br>
        <input type="checkbox" v-model="carpool.smoking">Smoking<br>
        <input type="checkbox" v-model="carpool.pets">Pets<br>
        <input type="checkbox" v-model="carpool.eatingDrinking">Eating/Drinking<br>
        <input type="checkbox" v-model="carpool.ac">AC<br>
        <input type="checkbox" v-model="carpool.chitChat"> Chit-chat<br>
      </div>
      <div style="margin-bottom: 10px;">
        <input type="checkbox" v-model="carpool.productDelivery"> Product Delivery<br>
        <div v-if="carpool.productDelivery">
          <label for="deliveryPrice">Delivery Price:</label>
          <input type="number" id="deliveryPrice" v-model="carpool.deliveryPrice" required style="border-radius: 10px; border-color: rgba(255, 255, 255, 0.5); height: 30px; margin-left: 10px; background-color: #FBAF56;">
        </div>
      </div>
      <button type="submit" @click="submitForm()" style="border-radius: 20px; width: 400px; height: 40px; background-color: #FBAF56; font-weight: bold; border-color: white;">Create Carpool</button>
    <p v-if="carpool.errormessage" style="color: red;">{{ carpool.errormessage }}</p>
  </div>
  </div>
  <footer class="footerComponent">
      <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      carpool: {
        date: '',
        startTime: '',
        startLocation: '',
        endLocation: '',
        viaRoute: '',
        vehicleType: '',
        vehicleNo: '',
        vehicleModel: '',
        seatsAvailable: 1,
        price: 0,
        music: false,
        smoking: false,
        pets: false,
        eatingDrinking: false,
        ac: false,
        chitChat: false,
        productDelivery: false,
        deliveryPrice: null,
        errormessage: "",
      }
    };
  },
  methods: {
    submitForm() {
      axios.post("http://127.0.0.1:8000/create-ride/", this.carpool)
        .then(response => {
          console.log(response.data);
          if (response.data.message == "Ride created successfully") {
            // Redirect to Home Page
            this.$router.push({ name: "Payment" });
          } 
        })
        .catch(error => {
          console.error(error);
          this.carpool.errormessage = "An error occurred during creation.";
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

.container {
  max-width: 1000px; 
  margin: 0 auto; 
}
.form-container {
  padding: 20px;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  max-width: 1000px; 
  margin: 0 auto; 
  text-align: left;
  height:700px;
}
button {
  display: block;
  margin: 0 auto;
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
</style>