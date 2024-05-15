<template>
  <div id="CreateCarpoolPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 150vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <div class="header-links">
        <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
        <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
        <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
      </div>
    </header>
    <h1 style="text-align: center">Payment</h1>
    <p style="text-align: center">Payment will be done after you accept the carpool requests by users through the QR code you upload here</p>
    <div class="content-box">
      <div class="button-container">
        <label for="qrUpload" class="custom-file-upload button-style">
          Upload QR
        </label>
        <input id="qrUpload" type="file" @change="handleFileChange" style="display:none;">
        <button @click="uploadPaymentPicture" class="button-style">Upload</button>
      </div>
      <p v-if="this.errormessage" style="color: red;">{{ this.errormessage }}</p>
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
      paymentPicture: null,
      errormessage: ""
    };
  },
  methods: {
    handleFileChange(event) {
      this.paymentPicture = event.target.files[0];
    },
    uploadPaymentPicture() {
      if (this.paymentPicture) {
        const formData = new FormData();
        formData.append('paymentPicture', this.paymentPicture);
        
        axios.post('http://127.0.0.1:8000/create-ride/payment-picture/', formData)
          .then(response => {
            console.log(response.data);
            if (response.data.message=="upload complete")
            {
              this.$router.push({ name: "HomePage" });
            }
          })
          .catch(error => {
            console.error('Error uploading picture:', error);
            this.errormessage = 'An error occurred while uploading the picture. Please try again.';
          });
      } else {
        console.warn('No picture selected');
        this.errormessage = 'No pictured selected. Please try again.';
      }
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

<style scoped>
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
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 20px;
  margin: 0s;
  text-align: left;
  margin-top:20px;
  height: 100px;
  width:1100px;
  margin-left:40px;
}

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.button-style {
  background-color: orange;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  margin-left: 10px;
  margin-right: 10px;
}
</style>

