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
    <h2 style="text-align:center;">My Profile</h2>
    <div v-if="driver">
      <div class="contents">
        <div>
          <img :src="driver.picture" alt="picture" class="profile-picture">
        </div>
        <label for="profilePicUpload" class="custom-file-upload button-style">
          Change Profile Picture
        </label>
        <input id="profilePicUpload" type="file" ref="ProfilepicFile" @change="handleProfilepicChange" style="display:none;">
        <h3>{{ driver.name }}</h3>
        <p>Age: {{ driver.age }}</p>
        <p>Email: {{ driver.email }}</p>
        <p>Occupation: {{ driver.occupation }}</p>
        <p>Phone Number: {{ driver.phoneNumber }}</p>
        <p>Rating: {{ driver.rating }}</p>
        <div v-if="!driver.driving_license">
          <label for="licenseupload" class="custom-file-upload button-style">
            Upload Driving license
          </label>
          <input id="licenseupload" type="file" ref="drivingLicenseFile" @change="handleDrivingLicenseChange" style="display:none;">
        </div>
        <button class="submit-button" @click="uploadFiles">Submit</button>
      </div>
    </div>
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
      driver: null,
      ProfilepicFile: null,
      drivingLicenseFile: null,
    };
  },
  created() {
    this.get_file();
  },
  methods: {
    handleProfilepicChange(event) {
      this.ProfilepicFile = event.target.files[0]; // Corrected property name
    },
    handleDrivingLicenseChange(event) {
      this.drivingLicenseFile = event.target.files[0];
    },
    uploadFiles() {
      const formData = new FormData();
      formData.append('profile_pic', this.ProfilepicFile);
      formData.append('driving_license', this.drivingLicenseFile);
      axios.post('http://127.0.0.1:8000/upload-edit/', formData)
      .then(response => {
          console.log(response.data);
          this.driver= null,
          this.ProfilepicFile= null,
          this.drivingLicenseFile= null,
          this.get_file()
         })
      .catch(error => {
           console.error('Error submitting review:', error);
         });
    },
    get_file(){
      axios.post("http://127.0.0.1:8000/my-profile/")
       .then(response => {
         this.driver = response.data;
       })
    .catch(error => {
         console.error('Error fetching driver profile:', error);
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
<style scoped>
  .profile-picture {
    width: 170px; 
    height: auto; 
  }

  .button-style {
    display: inline-block;
    cursor: pointer;
    padding: 8px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s;
  }

  .button-style:hover {
    background-color: #45a049;
  }

  .submit-button {
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .submit-button:hover {
    background-color: #0056b3;
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

  .contents {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
</style>


